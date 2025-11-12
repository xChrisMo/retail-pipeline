from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict

from .config import chunk_size, marts_path, min_quantity, min_unit_price, raw_input_path, staging_path
from .extract import extract_transactions
from .load import persist_tables
from .modeling import build_star_schema
from .quality import QualityResult, run_quality_checks
from .transform import enrich_transactions

LOGGER = logging.getLogger(__name__)


def _configure_logging(log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    handlers = [
        logging.FileHandler(log_path, mode="w", encoding="utf-8"),
        logging.StreamHandler(),
    ]
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=handlers,
    )


def run_pipeline() -> Dict[str, object]:
    project_root = Path.cwd()
    log_path = project_root / "pipeline.log"
    _configure_logging(log_path)

    LOGGER.info("Starting Online Retail pipeline")
    LOGGER.info(
        "Configuration: input=%s staging=%s marts=%s min_quantity=%s min_unit_price=%s chunk_size=%s",
        raw_input_path,
        staging_path,
        marts_path,
        min_quantity,
        min_unit_price,
        chunk_size,
    )

    #export
    raw_df = extract_transactions()
    LOGGER.info("Extracted %s rows from raw dataset", len(raw_df))

    #transform
    clean_df, stats = enrich_transactions(raw_df)
    LOGGER.info("Transformation stats: %s", stats)

    #model
    tables = build_star_schema(clean_df)
    for name, df in tables.items():
        LOGGER.info("Table %s has %s rows", name, len(df))

    #¢load
    outputs = persist_tables(tables)
    LOGGER.info("Persisted tables to disk: %s", outputs)

    #quality tests
    quality_results = run_quality_checks(tables)
    failed_checks = [result for result in quality_results if not result.passed]
    for result in quality_results:
        level = logging.INFO if result.passed else logging.ERROR
        LOGGER.log(level, "Quality check %s: %s (%s)", result.check_name, result.passed, result.details)

    if failed_checks:
        raise RuntimeError(
            "Data quality checks failed: "
            + ", ".join(f"{check.check_name} ({check.details})" for check in failed_checks)
        )

    return {
        "run_stats": stats,
        "table_counts": {name: len(df) for name, df in tables.items()},
        "quality_results": quality_results,
        "output_paths": outputs,
        "log_path": log_path,
    }


if __name__ == "__main__":
    run_pipeline()



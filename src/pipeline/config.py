from pathlib import Path
"""Simple configuration values for the pipeline."""

raw_input_path = Path("data/Online Retail.xlsx")
staging_path = Path("models/staging")
marts_path = Path("models/marts")

min_quantity = 1
min_unit_price = 0.01
chunk_size = None


def ensure_output_paths() -> None:
    # Creating output folders
    staging_path.mkdir(parents=True, exist_ok=True)
    marts_path.mkdir(parents=True, exist_ok=True)


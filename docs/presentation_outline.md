# Presentation Outline

## 1. Introduction
- Goal of the pipeline and dataset overview.

## 2. Architecture
- Diagram showing extract -> transform -> model -> quality -> load.
- Explain technology choices (Python, pandas, Parquet).

## 3. Data Ingestion & Assessment
- Key findings from profiling (missing customers, negative quantities).
- How logging captures data quality observations.

## 4. Pipeline Walkthrough
- Extraction logic and schema validation.
- Transformation steps and row counts removed.
- Dimensional modeling outputs.

## 5. Data Quality Framework
- Automated checks implemented.
- Behavior on failure and logging strategy.

## 6. Analytical Readiness
- Example queries or metrics enabled (revenue by country, products).
- Mention SQL DDL deliverable.

## 7. Assumptions & Future Work
- Any assumptions made (e.g., dropping missing customers).
- Potential enhancements (e.g., dbt, orchestration, additional dimensions).

## 8. Demo / Evidence
- Terminal screenshot of pipeline run output.
- Snapshot of `pipeline.log` and parquet row counts (e.g., using `pandas.read_parquet().head()`).
- Summary of deliverables and next steps.



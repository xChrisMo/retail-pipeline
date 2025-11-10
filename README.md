# Online Retail Data Pipeline

## Overview
This repository implements a data engineering pipeline for the UCI "Online Retail" dataset. The solution ingests the raw Excel data, profiles and cleans it, models a dimensional schema, runs automated data-quality checks, and persists analytics-ready parquet tables.

## Project Structure
- `Assessment.ipynb` - initial data profiling and exploration.
- `src/pipeline/` - Python package orchestrating extraction, transformation, modeling, loading, and quality checks.
- `models/` - generated parquet outputs (`marts` for fact tables, `staging` for dimensions).
- `docs/` - data model, data quality notes, data dictionary, architecture diagram, presentation outline.
- `sql/` - DDL scripts for the final schema.
- `requirements.txt` - Python dependencies.

## Prerequisites
- Python 3.11+ (tested with 3.14 via Homebrew).
- `virtualenv` ability to create a local environment.
- `pip` for package installation.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Pipeline
```bash
source .venv/bin/activate
python -m src.pipeline.run
```
Outputs:
- `pipeline.log` - structured log of the run.
- `models/marts/fact_sales.parquet`
- `models/staging/dim_customer.parquet`, `dim_product.parquet`, `dim_date.parquet`

## Configuration
Defaults live in `src/pipeline/config.py`. Update the path or threshold variables there if you need to point at a different input file or adjust filters.

## Data Model & Quality
- Star schema documented in `docs/data_model.md`.
- SQL DDL for warehouse creation in `sql/create_tables.sql`.
- Automated checks and handling described in `docs/data_quality.md`.
- Column-level definitions in `docs/data_dictionary.md`.

## Deliverables Summary
- Code (Python pipeline package)
- SQL scripts (`sql/create_tables.sql`)
- Documentation (`docs/*.md`, `README.md`, architecture diagram)
- Presentation deck (see outline in `docs/presentation_outline.md`)
- Screenshots/sample outputs (capture `pipeline.log`, parquet previews)

## Assumptions & Future Work
- Dropped transactions with missing customers or non-positive quantities/prices.
- Treated latest observed `UnitPrice` as product attribute; no product hierarchy provided.
- Potential enhancements: orchestrate with Airflow/Prefect, migrate transformations to dbt, expand data quality checks with Great Expectations, add unit tests.



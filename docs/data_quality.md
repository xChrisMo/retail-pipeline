# Data Quality Framework

## Automated Checks
The pipeline enforces the following rules before completing a run:

| Check | Description | Action |
| --- | --- | --- |
| `FactSalesQuantityPositive` | Ensures `quantity > 0` for every fact row. | Fail pipeline if any violations. |
| `FactSalesUnitPricePositive` | Requires `unit_price > 0`. | Fail pipeline if any violations. |
| `FactSalesCustomerExists` | Validates that every `customer_id` exists in `dim_customer`. | Fail pipeline if missing keys. |
| `FactSalesProductExists` | Validates that every `stock_code` exists in `dim_product`. | Fail pipeline if missing keys. |
| `FactSalesInvoiceLineUnique` | Confirms `invoice_line_id` uniqueness. | Fail pipeline if duplicates detected. |

The checks are written in `src/pipeline/quality.py` and executed at the end of the ETL run. Any failure raises a `RuntimeError`, breaking the pipeline and returning detailed counts in the exception message and log.

## Monitoring & Logging
* All checks and associated counts are logged in `pipeline.log`.
* Quality thresholds (minimum quantity and unit price) are configurable via `PipelineConfig`.
* The runtime summary (rows removed per filter, table row counts) is returned by `run_pipeline()` for downstream reporting.

## Handling Failures
When any check fails:
1. The pipeline breaks after logging the failure.
2. The output tables are still written for inspection.
3. Review `pipeline.log` and the exception message to identify the violating rows.
4. Adjust or fix source data before rerunning.



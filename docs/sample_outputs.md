# Sample Output Guidance

Use these examples for screenshots or appendix materials:

1. **Pipeline Run (Terminal)**
   ```bash
   source .venv/bin/activate
   python -m src.pipeline.run
   ```
   Capture the log output showing row counts and quality check results.

2. **Log Snippet**
   ```bash
   tail -n 20 pipeline.log
   ```
   Highlight transformation stats and quality check summary.

3. **Parquet Preview**
   ```python
   import pandas as pd
   df = pd.read_parquet("models/marts/fact_sales.parquet")
   df.head()
   ```
   Screenshot the first few rows to demonstrate schema.

4. **Quality Results Summary**
   ```python
   from src.pipeline.run import run_pipeline
   run_pipeline()
   ```
   Capture returned `run_stats` and `quality_results` dictionary from an interactive session.



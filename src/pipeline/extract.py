from __future__ import annotations

import pandas as pd

from .config import chunk_size, raw_input_path


def extract_transactions() -> pd.DataFrame:
    """Read the raw Excel file."""
    input_path = raw_input_path

    if not input_path.exists():
        raise FileNotFoundError(f"Expected raw input file at {input_path} but it was not found.")

    read_kwargs = {
        "engine": "openpyxl",
        "dtype": {
            "InvoiceNo": "string",
            "StockCode": "string",
            "Description": "string",
            "Quantity": "int64",
            "InvoiceDate": "datetime64[ns]",
            "UnitPrice": "float64",
            "CustomerID": "float64",
            "Country": "string",
        },
        "parse_dates": ["InvoiceDate"],
    }

    if chunk_size:
        chunks = pd.read_excel(input_path, chunksize=chunk_size, **read_kwargs)
        df = pd.concat(list(chunks), ignore_index=True)
    else:
        df = pd.read_excel(input_path, **read_kwargs)

    return df



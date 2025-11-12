from __future__ import annotations

from typing import Dict, Tuple

import pandas as pd

from .config import min_quantity, min_unit_price


def enrich_transactions(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, int]]:
    stats: Dict[str, int] = {"initial_rows": len(df)}

    mask_missing_customer = df["CustomerID"].isna()
    stats["missing_customer"] = int(mask_missing_customer.sum())
    df = df.loc[~mask_missing_customer].copy()

    mask_bad_quantity = df["Quantity"] < min_quantity
    stats["bad_quantity"] = int(mask_bad_quantity.sum())
    df = df.loc[~mask_bad_quantity]

    mask_bad_price = df["UnitPrice"] < min_unit_price
    stats["bad_unit_price"] = int(mask_bad_price.sum())
    df = df.loc[~mask_bad_price]

    df["CustomerID"] = df["CustomerID"].astype(int)

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    mask_invalid_dates = df["InvoiceDate"].isna()
    stats["invalid_invoice_date"] = int(mask_invalid_dates.sum())
    df = df.loc[~mask_invalid_dates]

    df["InvoiceYear"] = df["InvoiceDate"].dt.year
    df["InvoiceMonth"] = df["InvoiceDate"].dt.month
    df["InvoiceDay"] = df["InvoiceDate"].dt.day
    df["InvoiceWeek"] = df["InvoiceDate"].dt.isocalendar().week.astype(int)

    df["LineTotal"] = df["Quantity"] * df["UnitPrice"]

    stats["rows_retained"] = len(df)

    return df.reset_index(drop=True), stats



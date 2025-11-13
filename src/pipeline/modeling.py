from __future__ import annotations

from typing import Dict

import pandas as pd


def build_star_schema(clean_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Producing our fact and dimension tables."""
    fact_sales = clean_df[
        [
            "InvoiceNo",
            "StockCode",
            "CustomerID",
            "InvoiceDate",
            "Quantity",
            "UnitPrice",
            "LineTotal",
        ]
    ].copy()
    #creating a primary key for the facts table
    fact_sales["InvoiceLineId"] = fact_sales.apply(
        lambda row: f"{row['InvoiceNo']}-{row.name}", axis=1
    )
    fact_sales = fact_sales[
        [
            "InvoiceLineId",
            "InvoiceNo",
            "StockCode",
            "CustomerID",
            "InvoiceDate",
            "Quantity",
            "UnitPrice",
            "LineTotal",
        ]
    ]

    dim_customer = (
        clean_df[["CustomerID", "Country"]]
        .drop_duplicates()
        .rename(columns={"CustomerID": "CustomerKey"})
        .sort_values("CustomerKey")
        .reset_index(drop=True)
    )

    dim_product = (
        clean_df[["StockCode", "Description", "UnitPrice"]]
        .drop_duplicates()
        .rename(columns={"StockCode": "ProductKey", "UnitPrice": "UnitPriceLatest"})
        .sort_values("ProductKey")
        .reset_index(drop=True)
    )

    dim_date = (
        clean_df[["InvoiceDate", "InvoiceYear", "InvoiceMonth", "InvoiceDay", "InvoiceWeek"]]
        .drop_duplicates()
        .rename(columns={"InvoiceDate": "Date"})
        .sort_values("Date")
        .reset_index(drop=True)
    )
    dim_date["DateKey"] = dim_date["Date"].dt.strftime("%Y%m%d").astype(int)
    dim_date = dim_date[
        ["DateKey", "Date", "InvoiceYear", "InvoiceMonth", "InvoiceDay", "InvoiceWeek"]
    ]

    fact_sales = fact_sales.merge(
        dim_date[["Date", "DateKey"]],
        left_on="InvoiceDate",
        right_on="Date",
        how="left",
    )
    fact_sales = fact_sales.drop(columns=["Date"]).rename(columns={"DateKey": "InvoiceDateKey"})

    return {
        "fact_sales": fact_sales,
        "dim_customer": dim_customer,
        "dim_product": dim_product,
        "dim_date": dim_date,
    }



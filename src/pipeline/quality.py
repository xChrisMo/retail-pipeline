from __future__ import annotations

from typing import Dict, List

import pandas as pd


class QualityResult:
    def __init__(self, check_name: str, passed: bool, details: Dict[str, int]):
        self.check_name = check_name
        self.passed = passed
        self.details = details

    def __repr__(self) -> str:
        return (
            "QualityResult("
            f"check_name={self.check_name!r}, "
            f"passed={self.passed!r}, "
            f"details={self.details!r})"
        )


def run_quality_checks(tables: Dict[str, pd.DataFrame]) -> List[QualityResult]:
    """Helper function to SEQUENTIALLY run quality checks using the QualityResult classs"""
    
    results = []
    fact = tables["fact_sales"]

    # Quantity and UnitPrice quality checks
    bad_quantity = int((fact["Quantity"] <= 0).sum())
    results.append(
        QualityResult(
            check_name="FactSalesQuantityPositive",
            passed=bad_quantity == 0,
            details={"rows_with_bad_quantity": bad_quantity},
        )
    )

    bad_price = int((fact["UnitPrice"] <= 0).sum())
    results.append(
        QualityResult(
            check_name="FactSalesUnitPricePositive",
            passed=bad_price == 0,
            details={"rows_with_bad_price": bad_price},
        )
    )

    # DOing specific referential checks
    # Customer dimension first
    customer_keys = tables["dim_customer"]["CustomerKey"]
    missing_customers = int((~fact["CustomerID"].isin(customer_keys)).sum())
    results.append(
        QualityResult(
            check_name="FactSalesCustomerExists",
            passed=missing_customers == 0,
            details={"missing_customer_keys": missing_customers},
        )
    )

    # Product dimension now
    product_keys = tables["dim_product"]["ProductKey"]
    missing_products = int((~fact["StockCode"].isin(product_keys)).sum())
    results.append(
        QualityResult(
            check_name="FactSalesProductExists",
            passed=missing_products == 0,
            details={"missing_product_keys": missing_products},
        )
    )

    # Completeness: InvoiceLineId unique
    line_count = len(fact)
    unique_line_count = fact["InvoiceLineId"].nunique()
    results.append(
        QualityResult(
            check_name="FactSalesInvoiceLineUnique",
            passed=line_count == unique_line_count,
            details={"duplicate_lines": line_count - unique_line_count},
        )
    )

    return results



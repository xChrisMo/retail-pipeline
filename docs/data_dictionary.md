# Data Dictionary

## fact_sales
| Column | Type | Description |
| --- | --- | --- |
| `invoice_line_id` | TEXT | Surrogate key for the invoice line (`invoice_no` + line index). |
| `invoice_no` | TEXT | Invoice identifier from source system. |
| `stock_code` | TEXT | Product identifier. |
| `customer_id` | INTEGER | Foreign key to `dim_customer.customer_key`. |
| `invoice_date` | TIMESTAMP | Transaction timestamp. |
| `invoice_date_key` | INTEGER | Foreign key to `dim_date.date_key`. |
| `quantity` | INTEGER | Units sold on this line. |
| `unit_price` | NUMERIC | Recorded unit price. |
| `line_total` | NUMERIC | Calculated as `quantity * unit_price`. |

## dim_customer
| Column | Type | Description |
| --- | --- | --- |
| `customer_key` | INTEGER | Unique customer identifier. |
| `country` | TEXT | Customer country. |

## dim_product
| Column | Type | Description |
| --- | --- | --- |
| `product_key` | TEXT | Unique stock code for the product. |
| `description` | TEXT | Product description. |
| `unit_price_latest` | NUMERIC | Latest observed unit price for the product. |

## dim_date
| Column | Type | Description |
| --- | --- | --- |
| `date_key` | INTEGER | `YYYYMMDD` surrogate key. |
| `date` | DATE | Calendar date. |
| `invoice_year` | INTEGER | Year. |
| `invoice_month` | INTEGER | Month number. |
| `invoice_day` | INTEGER | Day of month. |
| `invoice_week` | INTEGER | ISO week number. |



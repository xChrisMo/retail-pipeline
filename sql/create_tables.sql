-- Schema for Online Retail analytics tables, basically our OLAP tables

CREATE TABLE dim_customer (
    customer_key INTEGER PRIMARY KEY,
    country TEXT NOT NULL
);

CREATE TABLE dim_product (
    product_key TEXT PRIMARY KEY,
    description TEXT,
    unit_price_latest NUMERIC
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    date DATE NOT NULL,
    invoice_year INTEGER NOT NULL,
    invoice_month INTEGER NOT NULL,
    invoice_day INTEGER NOT NULL,
    invoice_week INTEGER NOT NULL
);

CREATE TABLE fact_sales (
    invoice_line_id TEXT PRIMARY KEY,
    invoice_no TEXT NOT NULL,
    stock_code TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    invoice_date TIMESTAMP NOT NULL,
    invoice_date_key INTEGER REFERENCES dim_date(date_key),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC NOT NULL,
    line_total NUMERIC NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (stock_code) REFERENCES dim_product(product_key)
);


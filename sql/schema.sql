-- FACT TABLE
CREATE TABLE fact_transactions AS
SELECT
    row_number() OVER () AS transaction_id,
    "Time",
    "Amount",
    "Class" AS is_fraud
FROM transactions;

ALTER TABLE fact_transactions
ADD PRIMARY KEY (transaction_id);


-- DIMENSION : AMOUNT
CREATE TABLE dim_amount AS
SELECT DISTINCT
    CASE
        WHEN "Amount" < 50 THEN 'Low'
        WHEN "Amount" < 200 THEN 'Medium'
        ELSE 'High'
    END AS amount_category
FROM transactions;


-- DIMENSION : TIME
CREATE TABLE dim_time AS
SELECT DISTINCT
    "Time",
    FLOOR("Time"/3600) AS hour_bucket
FROM transactions;


-- PARTITION TABLE
CREATE TABLE transactions_partitioned (
    "Time" FLOAT,
    "Amount" FLOAT,
    "Class" INT
) PARTITION BY LIST ("Class");


-- PERFORMANCE INDEX
CREATE INDEX idx_fraud_status
ON fact_transactions(is_fraud);
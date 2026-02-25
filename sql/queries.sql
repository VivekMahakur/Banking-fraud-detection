-- ==============================
-- CTE : Fraud Percentage
-- ==============================

WITH fraud_stats AS (
    SELECT
        COUNT(*) FILTER (WHERE is_fraud = 1) AS fraud,
        COUNT(*) AS total
    FROM fact_transactions
)
SELECT
    fraud,
    total,
    ROUND((fraud * 100.0 / total),4) AS fraud_percentage
FROM fraud_stats;


-- ==============================
-- WINDOW FUNCTION
-- ==============================

SELECT
    "Amount",
    AVG("Amount") OVER() AS average_amount
FROM transactions
LIMIT 10;

-- ==============================
-- RANKING TRANSACTIONS
-- ==============================

SELECT
    transaction_id,
    "Amount",
    RANK() OVER (ORDER BY "Amount" DESC) AS amount_rank
FROM fact_transactions
LIMIT 10;

-- ==============================
-- RUNNING TOTAL
-- ==============================

SELECT
    transaction_id,
    "Amount",
    SUM("Amount") OVER (ORDER BY transaction_id)
        AS running_total
FROM fact_transactions
LIMIT 10;

-- ==============================
-- PERFORMANCE ANALYSIS
-- ==============================
-- Performance Before Optimization
EXPLAIN ANALYZE
SELECT *
FROM fact_transactions
WHERE is_fraud = 1;

-- Create Index
CREATE INDEX idx_fraud_status
ON fact_transactions(is_fraud);

-- Performance After Optimization
EXPLAIN ANALYZE
SELECT *
FROM fact_transactions
WHERE is_fraud = 1;
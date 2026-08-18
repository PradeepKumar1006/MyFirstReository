WITH cte AS (
    SELECT *,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS cat
    FROM Accounts
),
com AS (
    SELECT
        cat AS category,
        COUNT(DISTINCT account_id) AS accounts_count
    FROM cte
    GROUP BY 1
)

SELECT
    categories.category,
    COALESCE(com.accounts_count, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
) categories
LEFT JOIN com
ON categories.category = com.category;
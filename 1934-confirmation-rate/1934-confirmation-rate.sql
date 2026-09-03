WITH base AS (
    SELECT
        user_id,
        ROUND(AVG(action = 'confirmed'), 2) AS confirmation_rate
    FROM confirmations
    GROUP BY
        user_id
)
SELECT
    s.user_id,
    COALESCE(b.confirmation_rate, 0) AS confirmation_rate
FROM signups s
LEFT JOIN base b
    ON s.user_id = b.user_id;
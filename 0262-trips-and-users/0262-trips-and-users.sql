WITH cte AS (
    SELECT *
    FROM Trips
    WHERE client_id NOT IN (
        SELECT users_id
        FROM Users
        WHERE banned = 'Yes'
    )
    AND driver_id NOT IN (
        SELECT users_id
        FROM Users
        WHERE banned = 'Yes'
    )
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
)

SELECT
    request_at AS Day,
    ROUND(
        AVG(
            CASE
                WHEN status IN ('cancelled_by_driver', 'cancelled_by_client')
                THEN 1.0
                ELSE 0
            END
        ),
        2
    ) AS `Cancellation Rate`
FROM cte
GROUP BY request_at;
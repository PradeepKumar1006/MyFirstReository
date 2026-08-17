SELECT 
    product_id,
    CASE WHEN store1 IS NOT NULL THEN 'store1' END AS store,
    store1 AS price
FROM products
WHERE store1 IS NOT NULL

UNION

SELECT 
    product_id,
    CASE WHEN store2 IS NOT NULL THEN 'store2' END AS store,
    store2 AS price
FROM products
WHERE store2 IS NOT NULL

UNION

SELECT 
    product_id,
    CASE WHEN store3 IS NOT NULL THEN 'store3' END AS store,
    store3 AS price
FROM products
WHERE store3 IS NOT NULL;
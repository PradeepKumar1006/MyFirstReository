with cte as(
    select customer_number,count(customer_number) as c from orders group by 1 order by c desc
) select customer_number from cte limit 1
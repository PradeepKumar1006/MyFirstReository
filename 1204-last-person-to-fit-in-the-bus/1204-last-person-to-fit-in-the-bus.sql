with cte as (
    select *, SUM(weight) OVER(order by turn) as cumsum
    from queue
)
select person_name
from cte
where cumsum<=1000
order by cumsum desc
limit 1
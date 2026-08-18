with cte as (select *,sum(weight) over(order by turn) as ord from queue)
select person_name from cte where ord <= 1000 order by ord desc limit 1
with cte as (
    select *,if(actor_id = director_id,1,0) as cnt from actordirector
)select actor_id,director_id from cte group by 1,2 having count(cnt) >= 3
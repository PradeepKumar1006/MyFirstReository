with cte as (select user_id,count(user_id) as cnt 
from movierating group by 1 order by cnt desc),
test as (
    select u.name from users u left join cte c on u.user_id = c.user_id
    order by cnt desc ,name limit 1
), rating as (
    select movie_id, avg(rating) as rat from movierating 
    where created_at like '2020-02%'
    group by 1
),last as (select m.title from movies m left join rating r
on m.movie_id = r.movie_id
order by rat desc,m.title limit 1)
select name as results from test
union all 
select title as results from last
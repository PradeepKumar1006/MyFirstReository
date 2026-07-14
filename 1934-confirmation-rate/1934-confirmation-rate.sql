with cte as (
    select user_id,
    round(avg(action = 'confirmed'),2) as confirmation_rate
    from confirmations
    group by 1
)select s.user_id,coalesce(c.confirmation_rate,0) as confirmation_rate from signups s
left join cte c
on s.user_id = c.user_id
select
    round(
        count(distinct a.player_id)*1.0/
        (select count(distinct player_id) from activity),2
    ) as fraction
from activity a
join (
    select player_id,min(event_date) as first_login from activity group by player_id
) t
on a.player_id = t.player_id
and a.event_date = date_add(t.first_login, interval 1 day)
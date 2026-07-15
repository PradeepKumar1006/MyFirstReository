select contest_id,round(count(r.user_id)*100.0/(select count(u.user_id)from users u),2) as percentage from register r group by 1
order by 2 desc,1
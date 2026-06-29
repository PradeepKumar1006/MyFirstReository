select
firstname as firstName,
lastname lastName,
city,
state
from person p 
left join address a
on p.personid = a.personid
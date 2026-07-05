select email from person group by 1
having count(email) > 1
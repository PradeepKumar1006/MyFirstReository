select name from
employee
where id in (
    select managerid 
    from employee 
    group by 1 
    having count(managerId) >= 5)
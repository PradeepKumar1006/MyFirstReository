with cte as (select e.*,d.name as Department,dense_rank() over(partition by d.name order by e.salary desc) as rn
from employee e left join department d
on e.departmentid = d.id)
select Department,name as Employee, salary as Salary from cte where rn <= 3
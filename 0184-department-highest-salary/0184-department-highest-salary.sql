with cte as (
    select *,dense_rank() over(partition by departmentid order by salary desc) as rn from employee
)select d.name as Department, c.name as Employee, c.salary from cte c join department d on c.departmentid = d.id where c.rn = 1
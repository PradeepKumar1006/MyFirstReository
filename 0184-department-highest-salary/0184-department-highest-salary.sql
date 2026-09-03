with base as (
    select e.*,dense_rank() over(partition by departmentId order by salary desc) as rn,
    d.name as Department
    from employee e join department d
    on e.departmentId = d.id
)select department as Department,name as Employee,salary as Salary from base
where rn = 1
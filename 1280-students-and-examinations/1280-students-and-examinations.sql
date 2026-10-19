with
    cte as (
        select
            s.*,
            sub.*
        from students s cross join subjects sub
    )
    select
        c.student_id,
        c.student_name,
        c.subject_name,
        coalesce(count(e.subject_name),0) as attended_exams
    from cte c left join examinations e
        on c.student_id = e.student_id
        and c.subject_name = e.subject_name
    group by
        c.student_id,
        c.subject_name
    order by
        c.student_id,
        c.subject_name
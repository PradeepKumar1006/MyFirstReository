with cte as (
    select p.product_id,
    p.price,
    purchase_date ,
    units
    from prices p left join unitssold u
    on p.product_id = u.product_id
    and p.start_date <= purchase_date
    and purchase_date <= end_date
),prod as (
    select product_id,(price*units) as total_price,units from cte
)select product_id,
    round(coalesce(sum(total_price)*1.0/sum(units),0),2) as average_price from prod 
    group by product_id
select
product_id,coalesce((
    select p2.new_price from products p2 where p.product_id = p2.product_id
    and p2.change_date <= '2019-08-16'order by change_date desc limit 1
),10
) as price from products p group by 1
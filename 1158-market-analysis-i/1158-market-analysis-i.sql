select user_id buyer_id ,join_date,count(order_id) as orders_in_2019 from users u left join 
orders o on u.user_id = o.buyer_id
and o.order_date between '2019-01-01' and '2020-01-01'
group by 1,2
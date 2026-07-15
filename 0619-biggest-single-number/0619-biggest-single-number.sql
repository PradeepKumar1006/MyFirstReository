select max(num) num from 
(select num from mynumbers group by 1 having count(num) = 1) t
select 
city,
SUM(profit) as city_profit,
from `{{ project }}.{{ dataset_dest }}.orders_merged`
group by city
order by city_profit desc
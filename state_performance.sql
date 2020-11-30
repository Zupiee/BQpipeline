select 
state,
SUM(profit) as state_profit,
from `{{ project }}.{{ dataset_dest }}.orders_merged`
group by state
order by state_profit desc
select 
category,
SUM(quantity) as items_sold,
from `{{ project }}.{{ dataset_dest }}.orders_merged`
group by category

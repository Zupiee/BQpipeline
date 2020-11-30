select 
Order_ID as id,
order_date as `date`,
CustomerName as customer_name,
state,
city
from `{{ project }}.{{ dataset }}.orders_list` 
where order_id is not NULL 

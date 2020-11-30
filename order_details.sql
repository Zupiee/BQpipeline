select 
Order_ID as id,
amount,
profit,
quantity,
category,
sub_category
from `{{ project }}.{{ dataset }}.order_details`
where order_id is not NULL 

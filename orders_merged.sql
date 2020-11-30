select 
*
from `{{ project }}.{{ dataset_dest }}.orders_list` as A 
left join `{{ project }}.{{ dataset_dest }}.order_details` using (id)

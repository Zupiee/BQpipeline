select 
format_date("%b-20%Y",parse_date("%b-%Y",month_of_order_date)) as mod,  
category,
target
from `{{ project }}.{{ dataset }}.sales_target` 

 

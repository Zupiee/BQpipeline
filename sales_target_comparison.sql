with actual_sales as 
(
    select 
    format_date("%b-%Y",date) as month, 
    category, 
    SUM(amount)  as sales_amount
    from ecommerce.orders_merged 
    group by month , category
),
actual_vs_target as 
(
    select
    A.* , B.target
    from actual_sales as A JOIN `{{ project }}.{{ dataset_dest }}.sales_target` as B 
    ON A.month = B.mod AND A.category = B.category
)

select * , sales_amount-target as difference from actual_vs_target
 select name from salesperson
 except
 select a.name from orders c
 join salesperson a on c.sales_id = a.sales_id
 join company b on c.com_id = b.com_id
 where b.name = 'RED'
SELECT c.name AS Customers 
FROM Customers c
WHERE c.id NOT IN (select DISTINCT(customerId) from Orders);

-- Write your MySQL query statement below
SELECT v.customer_id, count(visit_id) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY v.customer_id
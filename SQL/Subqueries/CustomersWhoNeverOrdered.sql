SELECT c.name AS Customers 
FROM Customers c
WHERE c.id NOT IN (select DISTINCT(customerId) from Orders);
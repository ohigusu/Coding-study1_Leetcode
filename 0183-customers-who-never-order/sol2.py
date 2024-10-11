#using subquery
SELECT name as Customers 
FROM customers 
WHERE id NOT IN (SELECT DISTINCT customerId FROM orders)

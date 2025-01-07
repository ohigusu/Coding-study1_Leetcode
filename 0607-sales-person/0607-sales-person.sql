# Write your MySQL query statement below
#1. orders related to the company with the name "RED"
#2. not have any orders related to the company with the name "RED"
#3. names of all the salespersons who did not have any orders related to the company with the name "RED"
WITH tab1 AS (
SELECT o.sales_id
FROM Orders AS o 
    INNER JOIN Company AS c ON o.com_id=c.com_id
WHERE c.name = "RED"
)
SELECT s.name 
FROM SalesPerson AS s
    LEFT JOIN tab1 AS t ON s.sales_id = t.sales_id
WHERE t.sales_id IS NULL
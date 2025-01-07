SELECT s.name
FROM salesPerson AS s
WHERE s.sales_id NOT IN (
  SELECT o.sales_id 
  FROM orders as o
    LEFT JOIN company as c ON o.com_id = c.com_id WHERE name = "RED"
)

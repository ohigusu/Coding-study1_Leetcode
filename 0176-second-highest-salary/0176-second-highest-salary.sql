# Write your MySQL query statement below
WITH CTE AS (
    SELECT SUM(id) AS s
          ,salary
    FROM Employee 
    GROUP BY salary
    ORDER BY salary DESC LIMIT 2)

 SELECT (CASE WHEN COUNT(s)>1 THEN MIN(salary) ELSE null END) AS SecondHighestSalary
 FROM CTE


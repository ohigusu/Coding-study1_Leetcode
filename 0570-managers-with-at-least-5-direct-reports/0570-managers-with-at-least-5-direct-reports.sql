# Write your MySQL query statement below
SELECT b.name
FROM Employee AS a 
    INNER JOIN Employee AS b on a.managerId = b.id
GROUP BY b.id
    HAVING COUNT(DISTINCT a.id) >= 5


    
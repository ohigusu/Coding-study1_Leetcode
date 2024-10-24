SELECT name
FROM Employee
WHERE id  IN (SELECT (CASE WHEN COUNT(DISTINCT id) >= 5 THEN managerId END) AS managerId 
                        FROM Employee
                        GROUP BY managerId )

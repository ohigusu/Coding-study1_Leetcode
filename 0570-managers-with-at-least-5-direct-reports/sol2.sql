SELECT name
FROM Employee
WHERE id  IN (SELECT (CASE WHEN COUNT(DISTINCT id) >= 5 THEN managerId END) AS managerId 
                        FROM Employee
                        GROUP BY managerId )

#version2
SELECT name  
FROM EMPLOYEE 
WHERE id IN (SELECT managerId
              FROM EMPLOYEE
              GROUP BY ManagerId
                HAVing COUNT(*)>=5
)

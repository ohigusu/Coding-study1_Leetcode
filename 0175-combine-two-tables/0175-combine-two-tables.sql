# Write your MySQL query statement below
SELECT p.lastName
      ,p.firstName
      ,a.city
      ,a.state
FROM Person AS p
    LEFT JOIN Address AS a ON p.personId = a.personId

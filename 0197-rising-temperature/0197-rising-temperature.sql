# Write your MySQL query statement below
SELECT b.id AS Id
FROM Weather AS a
    INNER JOIN Weather AS b ON DATE_ADD(a.recordDate, INTERVAL 1 DAY) = b.recordDate
WHERE a.temperature < b.temperature 


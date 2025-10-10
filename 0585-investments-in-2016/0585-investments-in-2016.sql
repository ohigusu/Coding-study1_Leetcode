# Write your MySQL query statement below

WITH tab1 AS (
    SELECT *
    FROM Insurance
    GROUP BY lat,lon
        HAVING COUNT(DISTINCT pid) = 1
)
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM tab1
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(DISTINCT pid) > 1) 


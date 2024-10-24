# Write your MySQL query statement below
WITH tab AS(
    SELECT requester_id AS id
          ,accepter_id AS ac
    FROM RequestAccepted
    UNION 
    SELECT accepter_id AS id
          ,requester_id AS ac
    FROM RequestAccepted
)
SELECT id AS id
      ,COUNT(*) AS num
FROM tab
GROUP BY id
ORDER BY num DESC
LIMIT 1
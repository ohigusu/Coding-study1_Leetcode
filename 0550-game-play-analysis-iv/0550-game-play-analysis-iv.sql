# Write your MySQL query statement below
WITH first AS(
SELECT player_id
      ,DATE_ADD(MIN(event_date),INTERVAL 1 DAY) AS second_date
FROM Activity 
GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT (CASE WHEN b.player_id IS NOT NULL THEN b.player_id END))/COUNT(DISTINCT a.player_id),2) AS fraction
FROM Activity AS a 
    LEFT JOIN first AS b ON a.event_date = b.second_date
                            AND a.player_id = b.player_id
# Write your MySQL query statement below
SELECT player_id
      ,DATE_FORMAT(MIN(event_date),"%Y-%m-%d") AS first_login 
FROM Activity
GROUP BY player_id
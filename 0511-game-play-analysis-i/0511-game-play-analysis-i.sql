# Write your MySQL query statement below
SELECT player_id
      ,DATE_FORMAT(event_date,'%Y-%m-%d') AS first_login
FROM(
SELECT player_id
      ,event_date
      ,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS login_date
FROM Activity
) AS logintab
WHERE login_date = 1


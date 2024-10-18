# Write your MySQL query statement below
-- cancellation rate = (the number of canceled by client or driver requests with unbanned users)/(the total number of request with unbannd users)
-- each day between "2013-10-01" and "2013-10-03"
-- Round cancellation rate to two decimal ponts
SELECT 
    DATE_FORMAT(t.request_at, "%Y-%m-%d") AS Day,
    ROUND(SUM(t.status IN ('cancelled_by_driver', 'cancelled_by_client')) / COUNT(*), 2) AS "Cancellation Rate"
FROM 
    Trips t
JOIN 
    Users u1 ON t.client_id = u1.users_id
JOIN 
    Users u2 ON t.driver_id = u2.users_id
WHERE 
    u1.banned = 'No' 
    AND u2.banned = 'No'
    AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    Day;

-- List top 3 cities average temp (F) for July and August, in desc order.
SELECT city, AVG(value) AS avg_temp FROM temperatures
       WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

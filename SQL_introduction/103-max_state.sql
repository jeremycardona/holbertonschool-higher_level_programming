-- List top 3 max temps in (F), by state code.
SELECT state, MAX(value) AS max_temp FROM temperatures
       GROUP BY state ORDER BY state LIMIT 3;

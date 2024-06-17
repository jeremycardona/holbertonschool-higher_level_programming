-- list all records of second_table
-- dont list rows without a name
-- display score and name
-- records should be listed by descending score

SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;

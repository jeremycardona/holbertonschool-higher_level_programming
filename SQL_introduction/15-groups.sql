-- list the number of records with the same score in seconde_table
-- display the score
-- display the number of records for this score with the label number
-- list should be sorted by the number of records

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;

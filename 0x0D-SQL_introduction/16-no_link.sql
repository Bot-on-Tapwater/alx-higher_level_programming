-- Lists records but omit records that don't have a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

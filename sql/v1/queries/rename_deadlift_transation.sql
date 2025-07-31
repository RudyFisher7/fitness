BEGIN TRANSACTION;

UPDATE exercise
SET name = "Romanian Deadlift", description = "Posterior chain lift from Romania!"
WHERE name = "Deadlift"
;

SELECT * FROM exercise;

ROLLBACK;
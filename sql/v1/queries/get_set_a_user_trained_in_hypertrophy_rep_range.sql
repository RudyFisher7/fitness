WITH routine_ids AS (
	SELECT r.id AS r_id FROM routine r WHERE r.user_id = 1
)
SELECT * FROM routine_exercise_set res
JOIN routine_ids ON res.routine_id = routine_ids.r_id
LEFT JOIN exercise e ON res.exercise_id = e.id
WHERE res.reps > 5 AND res.reps < 13
;
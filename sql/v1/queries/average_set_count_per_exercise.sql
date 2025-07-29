WITH set_count AS (
	SELECT routine_id AS r_id, exercise_id AS e_id, COUNT(*) AS set_count FROM routine_exercise_set res
	GROUP BY routine_id, exercise_id
	ORDER BY routine_id
)
SELECT r_id, e_id, AVG(set_count.set_count)
FROM set_count
GROUP BY set_count.e_id
ORDER BY set_count.e_id
;
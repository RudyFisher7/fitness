SELECT routine_id, exercise_id, COUNT(*) AS set_count FROM routine_exercise_set
WHERE reps > 9
GROUP BY routine_id, exercise_id
HAVING set_count > 1
;
SELECT routine_id, exercise_id, COUNT(*) FROM routine_exercise_set res
GROUP BY routine_id, exercise_id
ORDER BY exercise_id
;
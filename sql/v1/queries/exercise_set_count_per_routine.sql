SELECT r.routine_id, COUNT(r.exercise_id) AS exercise_set_count FROM routine_exercise_set r
JOIN exercise e ON r.exercise_id = e.id GROUP BY r.routine_id;
SELECT res.exercise_id, e.name, COUNT(res.exercise_id) AS total_set_count FROM routine_exercise_set AS res
LEFT JOIN exercise AS e ON res.exercise_id = e.id
GROUP BY res.exercise_id
ORDER BY res.exercise_id
;
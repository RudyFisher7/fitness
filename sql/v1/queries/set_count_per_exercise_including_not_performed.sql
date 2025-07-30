SELECT e.id, e.name, COUNT(res.exercise_id) AS total_sets_performed FROM routine_exercise_set AS res
RIGHT JOIN exercise AS e ON res.exercise_id = e.id
GROUP BY res.exercise_id
ORDER BY e.id
;
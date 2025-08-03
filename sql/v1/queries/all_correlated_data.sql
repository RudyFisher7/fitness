SELECT * FROM user u
FULL JOIN routine r ON u.id = r.user_id
FULL JOIN routine_exercise_set res ON r.id = res.routine_id
FULL JOIN exercise e ON res.exercise_id = e.id
;
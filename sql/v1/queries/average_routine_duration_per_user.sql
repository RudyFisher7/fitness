SELECT u.id, r.user_id, u.display_name, AVG(r.duration_seconds) AS avg_routine_duration_seconds FROM user u
JOIN routine r ON u.id = r.user_id GROUP BY u.id;
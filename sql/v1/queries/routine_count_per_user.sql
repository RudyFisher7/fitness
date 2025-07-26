SELECT u.id, r.user_id, u.display_name, COUNT(r.id) AS routine_count FROM user u
JOIN routine r ON u.id = r.user_id GROUP BY u.id;
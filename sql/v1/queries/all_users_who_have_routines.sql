SELECT * FROM user
WHERE EXISTS (
	SELECT user_id FROM routine WHERE user_id = user.id
)
;
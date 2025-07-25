CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- in production, this should be a UUID or ULID or similar
	display_name TEXT,
	first_name TEXT,
	last_name TEXT,
	date_of_birth TEXT -- a date object
);


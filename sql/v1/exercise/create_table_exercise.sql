CREATE TABLE exercise (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- should be a UUID or similar in production
	name TEXT,
	description TEXT,
	muscle_groups INTEGER, -- see domain logic for bit flag
	work_types INTEGER, -- see domain logic for bit flag
	equipment INTEGER -- see domain logic for bit flag
);
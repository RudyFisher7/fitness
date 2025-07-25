CREATE TABLE routine (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- should be a UUID in production
    time_started TEXT, -- should be a datetime object
    duration_seconds INTEGER,
    name TEXT,
    description TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE
);
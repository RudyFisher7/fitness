CREATE TABLE routine_exercise (
    routine_id INTEGER,
    exercise_id INTEGER,
    index_in_routine INTEGER, -- the index into the list of exercises in the routine, to maintain order
    FOREIGN KEY(routine_id) REFERENCES routine(id),
    FOREIGN KEY(exercise_id) REFERENCES exercise(id)
);
CREATE TABLE routine_exercise_set (
    routine_id INTEGER,
    exercise_id INTEGER,
    index_in_routine INTEGER, -- the index into the list of exercises in the routine, to maintain order
    equipment INTEGER, -- see domain logic for enum
    duration INTEGER DEFAULT 0,
    distance INTEGER DEFAULT 0,
    reps INTEGER DEFAULT 0,
    resistance INTEGER DEFAULT 0, -- value encoding depends on equipment used
    FOREIGN KEY(routine_id) REFERENCES routine(id) ON DELETE CASCADE,
    FOREIGN KEY(exercise_id) REFERENCES exercise(id) ON DELETE SET NULL
);
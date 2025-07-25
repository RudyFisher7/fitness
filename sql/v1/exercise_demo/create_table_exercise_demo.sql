CREATE TABLE exercise_demo (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- use UUID in production
	exercise_id INTEGER, -- will be UUID in production
	cues TEXT,
	video_url TEXT, -- the URL to the video. NOTE:: the domain/UI layer will handle making the preview around this
	FOREIGN KEY(exercise_id) REFERENCES exercise(id)
);
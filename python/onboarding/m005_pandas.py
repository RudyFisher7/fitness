import pandas as pd
from datetime import datetime

favorite_exercises = pd.Series(["bench press", "bench press", "calf raise", "deadlift"], name="favorite_exercise")

dataframe_1 = pd.DataFrame({
    "user_name": ["Jane", "Jon", "Jeff", "Julie"],
    "date_of_birth": [datetime(1990, 1, 12), datetime(1972, 8, 3), datetime(1967, 9, 9), datetime(2000, 3, 30)],
    favorite_exercises.name: favorite_exercises,
})

print(dataframe_1)
print(dataframe_1.shape)
print(dataframe_1.describe())

# SELECT * FROM dataframe_1 WHERE date_of_birth < @y2k
# (Get every user that was born before Jan 1, 2000.)
y2k = datetime(2000, 1, 1)
print(dataframe_1.query("date_of_birth < @y2k"))
print(dataframe_1.query("date_of_birth.dt.year < 2000"))
print(dataframe_1[dataframe_1["date_of_birth"].dt.year.between(1900, 1999)])

print(dataframe_1.groupby(""))
import pandas as pd
from datetime import datetime

favorite_exercises = pd.Series(["bench press", "bench press", "calf raise", "deadlift", None], name="favorite_exercise")

dataframe_1 = pd.DataFrame({
    "user_name": ["Jane", "Jon", "Jeff", "Julie", "Jerald"],
    "date_of_birth": [datetime(1990, 1, 12), datetime(1972, 8, 3), datetime(1967, 9, 9), datetime(2000, 3, 30), datetime(2006, 3, 30)],
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

birth_decade = (dataframe_1["date_of_birth"].dt.year // 10) * 10
dataframe_2 = dataframe_1.copy(True)
dataframe_2["birth_decade"] = birth_decade

print(dataframe_2)
print(dataframe_2.groupby("birth_decade").count())

now = datetime.now()
ages = dataframe_1["date_of_birth"].apply(lambda dob: now.year - dob.year - (1 if (now.month, now.day) < (dob.month, dob.day) else 0))
dataframe_2["age"] = ages

print(dataframe_2)

print(f"median: {dataframe_2["age"].median()}, mean: {dataframe_2["age"].mean()}, std dev: {dataframe_2["age"].std()}")
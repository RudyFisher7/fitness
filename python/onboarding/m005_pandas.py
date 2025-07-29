import pandas as pd
from datetime import date

dataframe_1 = pd.DataFrame({
    "user_name": ["Jane", "Jon", "Jeff", "Julie"],
    "date_of_birth": [date(1990, 1, 12), date(1972, 8, 3), date(1967, 9, 9), date(2001, 3, 30)],
    "favorite_exercise": ["bench press", "bench press", "calf raise", "deadlift"],
})

print(dataframe_1)
import pandas as pd


def explore_data(filename):

    df = pd.read_csv(filename)

    total_students = len(df)

    subjects = ["Math", "Science", "English"]

    math_average = df["Math"].mean()
    highest_math_score = df["Math"].max()
    highest_math_student = df.loc[df["Math"] == highest_math_score, "Name"].values[0]

    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

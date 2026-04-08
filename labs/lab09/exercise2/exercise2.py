import pandas as pd


def compare_averages(filename):

    df = pd.read_csv(filename)

    Mean_Math = df["Math"].mean()
    Mean_Science = df["Science"].mean()
    Mean_English = df["English"].mean()

    averages = {
        "Math": Mean_Math,
        "Science": Mean_Science,
        "English": Mean_English
    }

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    return {
        "Math": Mean_Math,
        "Science": Mean_Science,
        "English": Mean_English,
        "best_subject": best_subject,
        "worst_subject":  worst_subject
    }

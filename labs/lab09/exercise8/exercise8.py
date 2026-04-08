import pandas as pd
import matplotlib.pyplot as plt

def plot_subject_maximums(filename):
    
    df = pd.read_csv(filename)

    max_scores = {
        "Math": df["Math"].max(),
        "Science": df["Science"].max(),
        "English": df["English"].max()
    }

    subjects = list(max_scores.keys())
    scores = list(max_scores.values())

    plt.plot(subjects, scores, marker='o')
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    plt.show()

    return len(df)

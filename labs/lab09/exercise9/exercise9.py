import pandas as pd
import matplotlib.pyplot as plt


def compare_subject_distributions(filename):
    df = pd.read_csv(filename)

    subjects = ["Math", "Science", "English"]
    plt.figure()
    for subject in subjects:
        plt.hist(df[subject], bins=10, alpha=0.5, label=subject)

    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title("Subject Score Distributions")
    plt.legend()
    plt.show()

    return len(df)

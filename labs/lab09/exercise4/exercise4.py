import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    
    df = pd.read_csv(filename)

    Science_Scores = df["Science"]

    plt.hist(Science_Scores, 10)
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")
    plt.show()

    return len(df)

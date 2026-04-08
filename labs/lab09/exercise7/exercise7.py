import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename)

    average_performance = df["PerformanceScore"].mean()
    min_years_required = 2

    candidates = df[
        (df["PerformanceScore"] >= average_performance) &
        (df["YearsOfService"] >= min_years_required)
    ]

    candidate_names = set(candidates["EmployeeName"].tolist())
    candidate_count = len(candidate_names)

    return {
        "average_performance": average_performance,
        "min_years_required": min_years_required,
        "candidate_count": candidate_count,
        "candidate_names": candidate_names
    }

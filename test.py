import pandas as pd

def get_funded_science_depts(filename):

    df = pd.read_csv(filename)
    
    avg_budget = df["Budget.2024"].mean()
    
    filtered = df[(df["Faculty Name"] == "Science")]
    filtered = filtered[(filtered["Budget.2024"] > avg_budget)]

    result = filtered[["Dept.ID", "Staff.Count"]]
    
    return result

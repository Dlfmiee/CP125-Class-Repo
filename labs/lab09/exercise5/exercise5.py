import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    subjects = ['Math', 'Science', 'English', 'Physics', 'Chemistry']
    
    names = []
    
    for i in range(len(df)):
        student = df.loc[i]
        
        is_high = True
        
        for subject in subjects:
            if student[subject] <= 85:
                is_high = False
        
        if is_high == True:
            names.append(student['Name'])
    
    return {
        "count": len(names),
        "names": set(names)
    }
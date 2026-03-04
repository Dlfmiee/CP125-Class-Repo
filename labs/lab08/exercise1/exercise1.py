# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    passing_scores = []
    
    f = open(input_file, "r")
    
    for line in f:
        line = line.strip()
        data = line.split()
        student_id = data[0]
        score = int(data[1])
        
        if score >= 80:
            passing_scores.append(f"{student_id} {score}")
    
    f.close()
    
    f = open(output_file, "w")
    
    for student in passing_scores:
        f.write(student + "\n")
    
    f.close()
    
    return len(passing_scores)

# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")

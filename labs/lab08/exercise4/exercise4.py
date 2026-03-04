# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:

import csv

def calculate_final_grades(input_file, output_file):
    total_grades = 0.0
    student_count = 0
    
    # Open input file
    f = open(input_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)
    
    # Open output file
    out = open(output_file, "w", newline="")
    writer = csv.writer(out)
    
    writer.writerow(["student_id", "final_grade"])
    
    for line in reader:
        student_id = line[0]
        midterm = float(line[1])
        final_exam = float(line[2])
        
        final_grade = (midterm * 0.4) + (final_exam * 0.6)
        
        total_grades += final_grade
        student_count += 1
        writer.writerow([student_id, f"{final_grade:.2f}"])
    
    f.close()
    out.close()
    
    average = total_grades / student_count
    
    return average  

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")

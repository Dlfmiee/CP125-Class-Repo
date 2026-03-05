"""def count_students(input_file, output_file):

    f = open(input_file, "r")
    
    count = len(f.readlines())
    f.close()

    f = open(output_file, "w")
    f.write("Total Students: " + str(count))
    f.close()


count_students("school_system/students/2024/names.txt","school_system/reports/summary.txt")
import csv

def check_low_attendance(input_file, output_file, threshold):
    f = open(input_file, "r",newline="")
    reader=csv.reader(f)
    header = next(reader)
    statistic_list = []
    
    for line in reader:
        name = line[0]
        attendance = float(line[1])
        if attendance < threshold:
            statistic_list.append(name)
            
    f.close()
    
    f = open(output_file, "w",newline="")
    for name in statistic_list:
        f.write(name + "\n")
    f.close()

check_low_attendance("school_system/students/2024/attendance.csv", "school_system/reports/statistics.txt", 75)

import csv

def filter_passing_students(config_file, scores_file, output_file):
    
    f = open(config_file, "r")
    w = open(scores_file, "r",newline="")
    
    threshold = f.readline()
    reader = csv.reader(w)
    next(reader)
    
    listscore = []
    
    for line in reader:
        if float(line[1]) >= float(threshold):
            listscore.append(f"{line[0]}: {line[1]}")
            
    f.close()
    w.close()
    
    f= open(output_file, "w",newline="")
    for name in listscore:
        f.write(name + "\n")
    f.close()

filter_passing_students("school_system/config/passing_grade.txt", "school_system/grades/midterm.csv", "school_system/reports/summary.txt")

def calculate_averages(midterm_file, final_file, output_file):
    
    midterm_file = open(midterm_file, "r",newline="")
    final_file = open(final_file, "r",newline="")
    
    midterm_reader = csv.reader(midterm_file)
    final_reader = csv.reader(final_file)
    
    next(midterm_reader)
    next(final_reader)
    
    averages = {}
    
    for line in midterm_reader:
        name = line[0]
        score = float(line[1])
        averages[name] = [score]
        
    for line in final_reader:
        name = line[0]
        score = float(line[1])
        if name in averages:
            averages[name].append(score)
        else:
            averages[name] = [score]
            
    midterm_file.close()
    final_file.close()
    
    f = open(output_file, "w",newline="")
    
    for name, scores in averages.items():
        average_score = sum(scores) / len(scores)
        f.write(f"{name}: {average_score:.1f}\n")
    f.close()

calculate_averages("school_system/grades/midterm.csv", "school_system/grades/final.csv", "school_system/reports/statistics.txt")

def generate_enrollment_report(old_file, new_file, output_file):
    
    f = open(old_file, "r")
    old_students = set(f)
    w = open(new_file, "r")
    new_students = set(w)
    
    f.close()
    w.close()

    all_students = old_students & new_students
    
    sorted_students = sorted(all_students)
    z = open(output_file, "w")
    
    z.write("Name\n")
    for name in sorted_students:
        z.write(name + "\n")

    z.close()
    
generate_enrollment_report("school_system/students/2024/names.txt", "school_system/students/2025/enrollment.txt", "school_system/reports/summary.csv")

import csv

def append_top_performers(input_file, output_file):
    
    f = open(input_file,'r')
    reader = csv.reader(f)
    next(reader)
    
    top_list = []
    
    for list in reader:
        name = list[0]
        attendance = list[1]
    
        if float(attendance) >= 90:
            top_list.append(f"{name},{attendance}")
            
    f.close()
    
    f = open(output_file, 'a', newline="")
    for name in top_list:
        f.write(name + "\n")
    
    f.close()
    
append_top_performers("school_system/students/2024/attendance.csv", "school_system/reports/top_performers.csv")"""

import csv

def append_new_students(new_file, target_file):
    f = open(new_file, 'r')
    reader = csv.reader(f)
    next(reader)
    
    new_students = []
    for line in reader:
        new_students.append(line)
    
    f.close()
    
    g = open(target_file, 'a', newline="")
    writer = csv.writer(g)
    
    for student in new_students:
        writer.writerow(student)
    
    g.close()

append_new_students("school_system/students/2025/new_students.csv", "school_system/grades/final.csv")
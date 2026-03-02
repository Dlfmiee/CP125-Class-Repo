def count_students(input_file, output_file):

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
# Name : MOHAMAD AIDIL FAHMI BIN SAHIMAT
# Description : Write a Python program that checks the grade for one student.

def determine_grade(mark):
    if mark >= 80:
        grade = "A"
    elif 60 <= mark <= 79:
        grade = "B"
    elif 50 <= mark <= 59:
        grade = "C"
    elif 40 <= mark <= 49:
        grade = "D"
    else:
        grade = "F"
    return grade

mark = float(input("Enter the student's mark: "))
grade = determine_grade(mark)
print(f"Mark: {mark}, Grade: {grade}")
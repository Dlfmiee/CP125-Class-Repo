import csv

def section1 ():

    f = open("bmi.csv","r")
    reader = csv.reader(f)

    print(f"File content: ")
    for row in reader:
        print(row)

    f.close()
    f = open("bmi.csv","r")
    reader = csv.reader(f)

    count = 0
    total = 0

    next(reader)
    for row in reader:
        height = float(row[1])
        total += height
        count += 1

    average = total/count

    print(f"Average height : {average}")

    f.close()

def section2 ():

    f = open("bmi.csv","a", newline="")
    gender = input("Enter gender : ")
    height = input("Enter height : ")
    weight = input("Enter weight : ")
    BMI = input("Enter BMI : ")

    writer = csv.writer(f)
    writer.writerow([gender,height,weight,BMI])
    print("New data added successfully")
    f.close()

    f = open("bmi.csv","r")
    print(f.read())

    f.close()
    
section1()
section2()
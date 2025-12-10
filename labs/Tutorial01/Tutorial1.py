# Scenario 2 , Code C and Code D

# Scenario 2
print(f"----- Scenario 2 -----")
def Determine_Scholarship(cgpa, tuition_fee):
    if 3.8 <= cgpa <= 4:
        waiver_percent = 1
        print("Full Scholarship Granted")
    elif 3.5 <= cgpa <= 3.79:
        waiver_percent = 0.5
        print("Partial Scholarship Granted")
    elif 3 <= cgpa <= 3.49:
        waiver_percent = 0.25
        print("Merit Award Granted")
    else:
        waiver_percent = 0
        print("No Scholarship Granted")
    
    waiver_amount = tuition_fee * waiver_percent
    amount_to_pay = tuition_fee - waiver_amount
    
    return amount_to_pay

result = Determine_Scholarship(3.6, 10000)
print(result)

# Code C
print(f"----- Code C -----")
def Calculate_Price(price,quantity):
    total = price * quantity
    if total > 100:
        total *= 0.9
    return total

Price1 = Calculate_Price(50,3)
Price2 = Calculate_Price(120,1)

print(f"Price 1: {Price1}")
print(f"Price 2: {Price2}")
print(f"Grand Total: {Price1 + Price2}")

# Code D
print(f"----- Code D -----")
def Calculate_Celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp1 = Calculate_Celsius(100)
temp2 = Calculate_Celsius(212)
temp3 = Calculate_Celsius(32)

print(f"Temp 1: {temp1}")
print(f"Temp 2: {temp2}")
print(f"Temp 3: {temp3}")

# Code E
print(f"----- Code E -----")
def Calculate_Profit(money,year_rate,years):
    total_profit = money * year_rate * years
    return total_profit

profit1 = Calculate_Profit(1000,0.05,3)
profit2 = Calculate_Profit(5000,0.04,5)
print(f"Profit 1: {profit1}")
print(f"Profit 2: {profit2}")

# Code F
print(f"----- Code F -----")
def Calculate_Cost(height,width):
    area = height * width
    paint = area / 350
    cost = paint * 45
    print(f"Wall : Area={area}, Paint={paint:.2f} gallons, Cost=RM{cost:.2f}")

Calculate_Cost(10,12)
Calculate_Cost(8,15)

# Code G
print(f"----- Code G -----")
def Calculate_NetPay(name,base,overtime_hours,overtime_rate):
    ot_pay = overtime_hours * overtime_rate
    gross_pay = base + ot_pay
    tax = gross_pay * 0.11
    net_pay = gross_pay - tax
    print("--- PAYSLIP ---")
    print(f"Name: {name}")
    print(f"Base: RM{base}")
    print(f"Overtime: RM{ot_pay}")
    print(f"Tax: RM{tax}")
    print(f"Net Pay: RM{net_pay}")

Calculate_NetPay("Ali",2000,10,15)
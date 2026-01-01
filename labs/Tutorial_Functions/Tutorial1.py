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

# Scenario 5
print(f"----- Scenario 5 -----")
def Calculate_RestaurantBill(price):
    if price >= 200:
        price *= 0.95
        Food_Service = price * 0.1
        Food_Tax = price * 0.06
        Final_Bill = Food_Service + Food_Tax
    else:
        Food_Service = price * 0.1
        Food_Tax = price * 0.06
        Final_Bill = Food_Service + Food_Tax
    return Final_Bill

result = Calculate_RestaurantBill(250)
print(result)

# Scenario 6
print(f"----- Scenario 6 -----")
def Calculate_ParkingFee(hours_parked,is_lost):
    if is_lost:
        return 50
    if hours_parked <= 3:
        fee = hours_parked * 3
    else:
        fee = 9 + ((hours_parked - 3) * 2)
    if fee > 20:
        fee = 20
    return fee
result = Calculate_ParkingFee(8, False)
print(result)

# Scenario 7
print(f"----- Scenario 7 -----")
def Calculate_TicketPrice(age, is_weekend, is_3D):
    if age < 12:
        price = 8
    elif 12 <= age <= 17:
        price = 12
    elif 18 <= age <= 59:
        price = 18
    else:
        price = 10

    if is_weekend:
        price += 3

    if is_3D:
        price += 5

    return price
result = Calculate_TicketPrice(23, True, True)
print(result)

# Scenario 8
print(f"----- Scenario 8 -----")
def Calculate_ElectricityBill(kWh):
    if kWh <= 200:
        bill = kWh * 0.218
    elif kWh <= 300:
        bill = (200 * 0.218) + ((kWh - 200) * 0.334)
    elif kWh <= 600:
        bill = (200 * 0.218) + (100 * 0.334) + ((kWh - 300) * 0.516)
    else:
        bill = (200 * 0.218) + (100 * 0.334) + (300 * 0.516) + ((kWh - 600) * 0.546)
    
    total_bill = bill + 3
    return total_bill

result = Calculate_ElectricityBill(450)
print(result)

# Scenario 9
print(f"----- Scenario 9 -----")
def Calculate_Insurance(age, claim):
    base_premium = 1000

    if age < 25:
        base_premium *= 1.30
    elif age > 60:
        base_premium *= 1.20

    if claim == 0:
        surcharge = base_premium * (-0.10)
    elif claim == 1:
        surcharge = 0
    else:
        surcharge = base_premium * 0.25

    total_premium = base_premium + surcharge
    return total_premium

result = Calculate_Insurance(28, 1)
print(result)


# Scenario 10
print(f"----- Scenario 10 -----")
def Calculate_WaterBill(water_usage):
    if water_usage <= 35:
        bill = water_usage * 0.57
    elif water_usage <= 50:
        bill = (35 * 0.57) + ((water_usage - 35) * 1.03)
    else:
        bill = (35 * 0.57) + (15 * 1.03) + ((water_usage - 50) * 1.5)
    total_bill = bill + 1.5 + 0.5
    return total_bill

result = Calculate_WaterBill(68)
print(result)

# Scenario 11
print(f"----- Scenario 11 -----")
def Calculate_Report(name,score1,score2,score3):
    average = (score1 + score2 + score3) / 3
    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"
    print(f"Student Name: {name}")
    print(f"Score 1: {score1}")
    print(f"Score 2: {score2}")
    print(f"Score 3: {score3}")
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}")

Calculate_Report("Ahmad",75,82,68)

# Scenario 12
print(f"----- Scenario 12 -----")
def Calculate_Order(price,quantity,stock):
    if quantity > 50:
        price *= 0.75
    elif quantity > 10 :
        price *= 0.85
    if quantity <= stock:
        return price * quantity
    else:
        return 0
    
result = Calculate_Order(80,45,60)
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

# Code H
print(f"----- Code H -----")
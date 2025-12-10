def calculate_car_insurance(age,claims_history):
    base = 1000
    if age < 25:
        base *= 1.3
    elif age > 60:
        base *= 1.2
    if claims_history == 0:
        base *= 0.9
    elif claims_history >= 2:
        base *= 1.25
    return base
result = calculate_car_insurance(28, 0)
print(result)
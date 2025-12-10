# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    if vehicle_type == "Electric":
        rate = 2
    elif vehicle_type == "Hybrid" and hour_24 >= 22 or hour_24 <= 6:
        rate = 2
    elif vehicle_type == "Hybrid":
        rate = 5
    else:
        rate = 5
    return rate

# Test your code here
print("Testing Dynamic Parking Rate...")

# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    num_tents = math.ceil(participants / tent_capacity)
    total_cost = (tent_price * num_tents) + (meal_price * participants)
    return total_cost
# Test your code here
print("Testing Camping Logistics...")
print(calculate_event_cost(10, 4, 50, 15))  # Example: 10 people, 4 per tent, RM50/tent, RM15/meal

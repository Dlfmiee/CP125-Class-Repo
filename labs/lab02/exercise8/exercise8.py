# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    bounce_height = current_height * 0.8
    return bounce_height

def is_ball_stopped(height):
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    current_height = start_height
    total_distance = start_height
    bounce_count = 0

    while not is_ball_stopped(current_height):
        current_height = calculate_bounce_height(current_height)
        total_distance += current_height * 2
        bounce_count += 1

    return bounce_count, total_distance

print("Testing Bouncing Ball Simulation...")

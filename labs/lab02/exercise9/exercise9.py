# Lab 02 Exercise 9: Level Up Calculator
# Write your code below:

def calculate_xp_required(current_level):
    return 100 * current_level

def can_level_up(xp_remaining, xp_required):
   return xp_remaining >= xp_required

def simulate_leveling(total_xp):
    level = 1
    xp_remaining = total_xp
    while True:
        xp_required = calculate_xp_required(level)
        if can_level_up(xp_remaining, xp_required):
            xp_remaining -= xp_required
            level += 1
        else:
            break
    return level, xp_remaining


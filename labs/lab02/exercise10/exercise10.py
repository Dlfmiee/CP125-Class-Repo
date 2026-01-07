def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    return (distance / 10) * 1.5

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    if is_sport_mode:
        return usage * 1.5
    return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    total_distance = distance * 2
    base_usage = calculate_base_usage(total_distance)
    total_usage = apply_mode_bonus(base_usage, is_sport_mode)
    return current_battery >= total_usage

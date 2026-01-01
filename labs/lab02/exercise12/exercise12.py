<<<<<<< HEAD
=======

>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b
def is_critical_hit(luck):
    """
    Returns True if luck is above 70.
    """
<<<<<<< HEAD
    return luck > 70
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def calculate_raw_damage(base_attack, is_crit):
    """
    Doubles the base attack if it's a critical hit.
    """
<<<<<<< HEAD
    if is_crit:
        return base_attack * 2
    return base_attack
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def calculate_final_health(current_health, raw_damage, defense):
    """
    Calculates final health after damage.
    Actual damage = raw_damage - defense.
    Damage cannot be negative.
    Final health cannot go below 0.
    """
<<<<<<< HEAD
    actual_damage = max(0, raw_damage - defense)
    return max(0, current_health - actual_damage)
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

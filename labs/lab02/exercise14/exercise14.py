<<<<<<< HEAD
=======

>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b
def is_safe_time(hour, temperature):
    """
    Returns False if 10 <= hour <= 16 (10 AM to 4 PM),
    UNLESS temperature > 40.
    """
<<<<<<< HEAD
    if 10 <= hour <= 16 and temperature <= 40:
        return False
    return True
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def needs_moisture(moisture_level):
    """
    Returns True if moisture < 30.
    """
<<<<<<< HEAD
    return moisture_level < 30
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def should_trigger_pump(moisture, hour, temp):
    """
    Returns True if it needs moisture AND is a safe time.
    """
<<<<<<< HEAD
    return needs_moisture(moisture) and is_safe_time(hour, temp)
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

<<<<<<< HEAD
=======

>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b
def get_rate_per_kg(destination):
    """
    Returns 5.0 for Domestic, 15.0 for International.
    """
<<<<<<< HEAD
    if destination == "Domestic":
        return 5.0
    elif destination == "International":
        return 15.0
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def get_express_charge(is_express):
    """
    Returns 10.0 if is_express is True, otherwise 0.0.
    """
<<<<<<< HEAD
    if is_express:
        return 10.0
    return 0.0
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

def calculate_shipping_quote(weight, destination, is_express):
    """
    Calculates final quote: (weight * rate) + express_charge
    """
<<<<<<< HEAD
    rate = get_rate_per_kg(destination)
    charge = get_express_charge(is_express)
    return weight * rate + charge
=======
    # TODO: Implement this function
    pass
>>>>>>> cfa6238a06b91e1e1e3c6b5d7f15d0b46fd1047b

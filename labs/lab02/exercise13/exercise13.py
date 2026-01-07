def get_rate_per_kg(destination):
    """
    Returns 5.0 for Domestic, 15.0 for International.
    """
    if destination == "Domestic":
        return 5.0
    elif destination == "International":
        return 15.0

def get_express_charge(is_express):
    """
    Returns 10.0 if is_express is True, otherwise 0.0.
    """
    if is_express:
        return 10.0
    return 0.0

def calculate_shipping_quote(weight, destination, is_express):
    """
    Calculates final quote: (weight * rate) + express_charge
    """
    rate = get_rate_per_kg(destination)
    charge = get_express_charge(is_express)
    return weight * rate + charge

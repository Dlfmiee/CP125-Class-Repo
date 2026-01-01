def is_valid_multiple(amount):
    """
    Checks if the amount is a multiple of RM10.
    """
    return amount > 0 and amount % 10 == 0

def is_balance_sufficient(amount, balance):
    """
    Checks if the balance is enough for the withdrawal.
    """
    return balance >= amount

def process_withdrawal(amount, balance):
    """
    Processes the withdrawal.
    Returns the new balance if successful.
    Returns "Invalid Amount" if not a multiple of 10.
    Returns "Insufficient Funds" if balance is too low.
    """
    if not is_valid_multiple(amount):
        return "Invalid Amount"
    if not is_balance_sufficient(amount, balance):
        return "Insufficient Funds"
    return balance - amount
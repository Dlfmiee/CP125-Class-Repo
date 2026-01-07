

def find_momentum_days(prices):
    if len(prices) < 2:
        return []
    
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])

    momentum_days = []
    for i in range(1, len(changes)):
        if changes[i] > changes[i-1]:
            momentum_days.append(i + 1) 
    return momentum_days


# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]

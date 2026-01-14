
def find_largest_drop(readings):

    max_drop = 0

    for i in range(len(readings) - 1):
        if readings[i] > readings[i+1]:
            drop = readings[i] - readings[i+1]
            if drop > max_drop:
                max_drop = drop

    return max_drop

# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5

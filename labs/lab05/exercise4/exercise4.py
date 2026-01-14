import math
def filter_query_times(times):
    if len(times) == 0:
        return []
    
    mean = sum(times)/len(times)
    variance = sum((i - mean) ** 2 for i in times) / len(times)
    std_dev = math.sqrt(variance)
    upper_limit = mean + std_dev

    filtered = []
    for i in times:
        if i <= upper_limit:
            filtered.append(i)

    filtered.sort()
    return filtered

# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]

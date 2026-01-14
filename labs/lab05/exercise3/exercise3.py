
def find_bottleneck_index(traceroute):
    max_diff = 0
    bottleneck_index = 0

    for i in range(len(traceroute) - 1):
        hop_number1, latency_in_ms1 = traceroute[i]
        hop_number2, latency_in_ms2 = traceroute[i + 1]

        difference_latency = latency_in_ms2 - latency_in_ms1
        if difference_latency > max_diff:
            max_diff = difference_latency
            bottleneck_index = i

    return bottleneck_index
# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1

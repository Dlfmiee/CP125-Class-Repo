
def find_slow_endpoints(api_calls, threshold):
    endpoint_latencies = {}

    for endpoint, latency, status in api_calls:
        if status == 200:
            endpoint_latencies.setdefault(endpoint, []).append(latency)

    slow = []
    for endpoint, latencies in endpoint_latencies.items():
        if len(latencies) < 2:
            continue
        avg = sum(latencies) / len(latencies)
        if avg > threshold:
            slow.append(endpoint)

    return sorted(slow)


api_calls = [
    ("/login", 45, 200), 
    ("/login", 120, 200), 
    ("/data", 80, 200),
    ("/login", 50, 500),
    ("/data", 95, 200), 
    ("/search", 30, 200),
    ("/health", 150, 200)
]

result = find_slow_endpoints(api_calls, 70)
print(f"Slow endpoints: {result}")

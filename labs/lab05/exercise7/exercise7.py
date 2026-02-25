
def find_conflicting_ports(rules):
    first_action = {}
    conflicts = {}

    for rule_id, port, action in rules:
        if port not in first_action:
            first_action[port] = action
        else:
            if action != first_action[port] and port not in conflicts:
                conflicts[port] = rule_id

    return sorted([(p, rid) for p, rid in conflicts.items()], key=lambda x: x[0])


rules = [
    (1, 80, "ALLOW"), 
    (2, 443, "ALLOW"), 
    (3, 80, "BLOCK"),
    (4, 22, "BLOCK"), 
    (5, 443, "BLOCK"), 
    (6, 8080, "ALLOW")
]

result = find_conflicting_ports(rules)
print(f"Conflicts: {result}")

rules2 = [
    (1, 80, "ALLOW"), 
    (2, 80, "ALLOW"), 
    (3, 443, "BLOCK")
]

result2 = find_conflicting_ports(rules2)
print(f"Conflicts: {result2}")

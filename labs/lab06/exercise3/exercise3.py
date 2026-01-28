def audit_blocklists(list_a, list_b, list_c):

    universal = set()

    for item in list_a:
        if item in list_b and item in list_c:
            universal.add(item)

    redundant = set()

    for item in list_a:
        if item in list_b or item in list_c:
            redundant.add(item)

    for item in list_b:
        if item in list_c:
            redundant.add(item)

    unique_a = set()
    
    for item in list_a:
        if item not in list_b and item not in list_c:
            unique_a.add(item)

    return universal, redundant, unique_a

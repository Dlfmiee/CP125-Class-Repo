def find_at_risk_departments(departments, threshold):
    at_risk = []

    for dept, students in departments.items():
        if not students:
            continue

        scores = students.values()
        below = sum(1 for s in scores if s < threshold)
        if below > (len(students) / 2):
            at_risk.append(dept)

    return sorted(at_risk)


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))

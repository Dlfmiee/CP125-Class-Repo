def match_specialists(candidates_list, project_requirements):

    skill_counts = {}
    for candidate in candidates_list:
        name = candidate[0]
        skills = candidate[1]
        for skill in skills:
            if skill in skill_counts:
                skill_counts[skill] += 1
            else:
                skill_counts[skill] = 1


    rare_skills = set()
    for skill in skill_counts:
        if skill_counts[skill] < 3:
            rare_skills.add(skill)

    result = []
    for candidate in candidates_list:
        name = candidate[0]
        skills = candidate[1]

        has_all_required = True
        for req in project_requirements:
            if req not in skills:
                has_all_required = False
                break

        if has_all_required:
            rare_in_candidate = skills & rare_skills

            if rare_in_candidate:
                result.append((name, rare_in_candidate))

    return result

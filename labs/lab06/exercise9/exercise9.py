def find_qualified_students(student_records, required_courses):
    qualified = []
    
    for student_id, completed in student_records:
        common = completed & required_courses
        
        if common == required_courses:
            qualified.append(student_id)
    
    return sorted(qualified)

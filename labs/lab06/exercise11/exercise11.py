def get_student_courses(enrollments, student_id):

    courses = set()
    for sid, course in enrollments:
        if sid == student_id:
            courses.add(course)
    return courses


def find_missing_courses(completed_courses, required_courses):

    return required_courses - completed_courses


def build_student_report(students, enrollments, required_courses):

    incomplete = []

    for student_id in students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)

        if missing:
            incomplete.append((student_id, len(missing)))

    return sorted(incomplete, key=lambda x: (-x[1], x[0]))


def find_incomplete_students(enrollments, required_courses):

    students = set()
    for student_id, _ in enrollments:
        students.add(student_id)

    return build_student_report(students, enrollments, required_courses)

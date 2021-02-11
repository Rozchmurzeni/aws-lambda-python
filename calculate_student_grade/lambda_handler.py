from calculator import calculate


def handle(event, context):
    return produce_result(calculate, event['lectureGrade'], event['exerciseGrade'], event['workshopGrade'])


def produce_result(calculate_function, lecture_grade, exercise_grade, workshop_grade):
    final_grade, has_passed = calculate_function(lecture_grade, exercise_grade, workshop_grade)
    return {
        'finalGrade': final_grade,
        'hasPassed': has_passed
    }

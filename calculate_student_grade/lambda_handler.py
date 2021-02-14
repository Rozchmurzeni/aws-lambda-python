from calculator import calculate


def handle(event, context):
    return produce_result(event['lectureGrade'], event['exerciseGrade'], event['workshopGrade'])


def produce_result(lecture_grade, exercise_grade, workshop_grade):
    final_grade, has_passed = calculate(lecture_grade, exercise_grade, workshop_grade)
    return {
        'finalGrade': final_grade,
        'hasPassed': has_passed
    }

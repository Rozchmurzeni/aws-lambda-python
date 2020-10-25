from calculator import calculate


def handle(event, context):
    return produce_result(calculate, event['lectureGrade'], event['exerciseGrade'], event['workshopGrade'])


def produce_result(calculate_function, lecture_grade, exercise_grade, workshop_grade):
    return {
        'statusCode': 200,
        'body': calculate_function(lecture_grade, exercise_grade, workshop_grade)
    }

LECTURE_WEIGHT = 0.2
EXERCISE_WEIGHT = 0.3
WORKSHOP_WEIGHT = 0.5
GRADE_TO_PASS = 3


def calculate(lecture_grade, exercise_grade, workshop_grade):
    raw_final_grade = LECTURE_WEIGHT * lecture_grade \
                      + EXERCISE_WEIGHT * exercise_grade \
                      + WORKSHOP_WEIGHT * workshop_grade
    final_grade = round_to_nearest_half(raw_final_grade)
    has_passed = final_grade >= GRADE_TO_PASS \
                 and lecture_grade >= GRADE_TO_PASS \
                 and exercise_grade >= GRADE_TO_PASS \
                 and workshop_grade >= GRADE_TO_PASS
    return final_grade, has_passed


def round_to_nearest_half(number_to_round):
    return round((number_to_round * 2) / 2)

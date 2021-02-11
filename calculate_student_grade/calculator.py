LECTURE_WEIGHT = 0.2
EXERCISE_WEIGHT = 0.3
WORKSHOP_WEIGHT = 0.5
GRADE_TO_PASS = 3


def calculate(ls):
    raw_final_grade = LECTURE_WEIGHT * lecture_grade \
                      + EXERCISE_WEIGHT * exercise_grade \
                      + WORKSHOP_WEIGHT * workshop_grade

    final_grade = round_to_nearest_half(raw_final_grade)
    return final_grade, final_grade >= GRADE_TO_PASS


def round_to_nearest_half(number_to_round):
    return round((number_to_round * 2) / 2)

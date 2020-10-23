import sys
import unittest

sys.path.insert(0, './calculate_student_grade')

from calculate_student_grade.lambda_handler import handle


class TestReturnCorrectResponse(unittest.TestCase):
    def test_handle(self):
        response = handle(None, None)

        self.assertEqual(response['body'], 5)
        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()

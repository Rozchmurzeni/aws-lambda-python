import unittest
from calculate_student_grade.lambda_handler import handle


class TestIsStatusProperToCheckDrift(unittest.TestCase):
    def test_handle(self):
        result = handle()

        self.assertEqual(result.body, 5)
        self.assertEqual(result.statusCode, 200)


if __name__ == '__main__':
    unittest.main()

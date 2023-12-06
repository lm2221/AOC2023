import unittest
from digits_strings import get_calibration_score_q1, get_calibration_score_q2

class TestCalibrationFunctions(unittest.TestCase):

    def test_get_calibration_score_q1_1(self):
        # Assuming a file with content "one two three"
        file_path = 'test_file_q1.txt'
        with open(file_path, 'w') as test_file:
            test_file.write("six6four")

        result = get_calibration_score_q1(file_path)
        self.assertEqual(result, 66)  # Replace with the expected result based on your input file

    def test_get_calibration_score_q2_1(self):
        # Assuming a file with content "one two three"
        file_path = 'test_file_q2.txt'
        with open(file_path, 'w') as test_file:
            test_file.write("twone")

        result = get_calibration_score_q2(file_path)
        self.assertEqual(result, 21)  # Replace with the expected result based on your input file

    def test_get_calibration_score_q2_8(self):
        # Assuming a file with content "one two three"
        file_path = 'test_file_q3.txt'
        with open(file_path, 'w') as test_file:
            test_file.write("two1nine\n")
            test_file.write("eightwothree\n")
            test_file.write("abcone2threexyz\n")
            test_file.write("xtwone3four\n")
            test_file.write("4nineeightseven2\n")
            test_file.write("zoneight234\n")
            test_file.write("7pqrstsixteen\n")

        result = get_calibration_score_q2(file_path)

        self.assertEqual(result, 281)  # Replace with the expected result based on your input file



if __name__ == '__main__':
    unittest.main()
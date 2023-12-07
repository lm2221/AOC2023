import unittest
from boats import *

class TestBoats(unittest.TestCase):

    def test_boats(self):
        # Assuming a file with content "one two three"
        test_file = '../data/test_file_6.txt'

        # with open(file_path, 'w') as test_file:
        #     test_file.write("Time:      7  15   30\n")
        #     test_file.write("Distance:  9  40  200\n")

        result = boats_question1(test_file)
        self.assertEqual(result, 288)

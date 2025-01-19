import unittest
from ex1 import safe_division
from ex2 import convert_to_int
from ex3 import read_file
from ex4 import set_age, NegativeAgeError
from ex5 import process_input

class TestExercises(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(safe_division(10 , 2), 5)
        self.assertEqual(safe_division(10, 0), "division by zero is not possible")

    def test_ex2(self):
        self.assertEqual(convert_to_int("10"), 10)
        self.assertEqual(convert_to_int("invalid"), "invalid input")
        self.assertEqual(convert_to_int(1.2), 1)

    def test_ex3(self):
        self.assertEqual(read_file("jump"), "the file jump exists") 


    def test_ex4(self):
        self.assertEqual(set_age(25), 25)
        with self.assertRaises(NegativeAgeError):
            set_age(-25)

    def test_ex5(self):
        self.assertEqual(process_input("10"), 1.0)
        self.assertEqual(process_input("invalid"), "invalid input")

if __name__ == '__main__':
    unittest.main()

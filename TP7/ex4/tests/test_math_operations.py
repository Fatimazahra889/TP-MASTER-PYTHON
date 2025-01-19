import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.math_operations import add, substract, multiply, divide
from src.string_operations import concatenate, capitalize

class TestModul(unittest.TestCase):
    def test_add(Self):
        Self.assertEqual(add(1,2),3)
    
    def test_substract(Self):
        Self.assertEqual(substract(2,1),1)

    def test_multiply(Self):
        Self.assertEqual(multiply(2,3),6)

    def test_divide(Self):
        Self.assertEqual(divide(6,3),2)

    def test_concatenate(Self):
        Self.assertEqual(concatenate("Hello","world"),"Helloworld")

    def test_capitalize(Self):
        Self.assertEqual(capitalize("hello"),"HELLO")

if __name__ == '__main__':
    unittest.main()

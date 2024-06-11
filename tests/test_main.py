# tests/test_main.py
import unittest
import sympy as sp
from tensor_framework.main import calculate_tensor_expression
from tensor_framework.utils import create_tensor, tensor_contraction, tensor_addition, tensor_multiplication

class TestTensorFramework(unittest.TestCase):
    def test_simplification(self):
        expression = "2*x + 3*x"
        result = calculate_tensor_expression(expression)
        self.assertEqual(result, "5*x")

    def test_invalid_expression(self):
        expression = "2*x +"
        result = calculate_tensor_expression(expression)
        self.assertTrue("Error" in result)

    def test_create_tensor(self):
        tensor = create_tensor(['a', 'b', 'c', 'd'], (2, 2))
        self.assertEqual(tensor.shape, (2, 2))
        self.assertEqual(str(tensor[0, 0]), 'a')

    def test_tensor_contraction(self):
        tensor = create_tensor(['a', 'b', 'c', 'd'], (2, 2))
        contracted_tensor = tensor_contraction(tensor, (0, 1))
        self.assertEqual(contracted_tensor, sp.Symbol('a') + sp.Symbol('b') + sp.Symbol('c') + sp.Symbol('d'))

if __name__ == '__main__':
    unittest.main()


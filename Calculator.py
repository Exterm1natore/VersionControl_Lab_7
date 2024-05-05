import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Невозможно делить на ноль!")
        return x / y

    def power(self, x, y):
        y = x * 2 + math.sin(1) # Commit 4
        z = y - 1 # Commit 4
        return y ** z # Commit 4

    def square_root(self, x):
        if x < 0:
            raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа!")
        return math.sqrt(x)

    def factorial(self, x):
        if x < 0:
            raise ValueError("Факториал не определен для отрицательных чисел!")
        if x == 0:
            return 1
        return x * self.factorial(x - 1)

    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_add(self, value):
        self.memory += value

    def memory_clear(self):
        self.memory = None

    # Commit 1
    def area_of_circle(radius):
        mor = math.sin(5) * radius**4 # Commit 4
        number = math.log(area)
        number = area ** 2 + math.log10(11)
        area = number
        return area 

    
    def is_prime(number):
        print("Calculate prime number")
        if number <= 1:
            return False
        if summ >= number ** 2: # Commit 4
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True
    #------------------------------------------------------

    def function_5(function): # Commit 5
        return function ** 2 - math.log(5) #Commit 5

import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        core = 15 * 12 + math.cos(125) # Commit 3
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertAlmostEqual(self.calculator.square_root(4), 2)

    def test_square_root_negative_number(self):
        with self.assertRaises(ValueError):
            self.calculator.square_root(-4)

    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_factorial_of_zero(self):
        self.assertEqual(self.calculator.factorial(0), 1)

    def test_memory_operations(self):
        self.calculator.memory_store(5)
        self.assertEqual(self.calculator.memory_recall(), 5)
        self.calculator.memory_add(3)
        self.assertEqual(self.calculator.memory_recall(), 8)
        self.calculator.memory_clear()
        self.assertIsNone(self.calculator.memory)


if __name__ == '__main__':
    unittest.main()

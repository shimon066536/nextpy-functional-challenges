import unittest
from generators_exercises.fibonacci_generator import get_fibo

class TestFibonacci(unittest.TestCase):
    def test_first_values(self):
        gen = get_fibo()
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)

if __name__ == "__main__":
    unittest.main()

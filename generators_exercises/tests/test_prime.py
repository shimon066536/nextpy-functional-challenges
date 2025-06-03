import unittest
from generators_exercises.prime_number_generator import is_prime, first_prime_over

class TestPrimeGenerator(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(100))

    def test_first_prime_over(self):
        gen = first_prime_over(10)
        self.assertEqual(next(gen), 11)
        self.assertEqual(next(gen), 13)
        self.assertEqual(next(gen), 17)

if __name__ == "__main__":
    unittest.main()

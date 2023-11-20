import unittest

from mpmath import zetazero

from increasing_function import find


class TestFindFunction(unittest.TestCase):
    def test_increasing_function_value_in_range(self):
        """
        Check that the function evaluation value is within the range
        """

        def test_function(n):
            return float(n)

        self.assertEqual(find(test_function, 5, 0, 10), 5)

    def test_increasing_function_value_not_in_range(self):
        """
        Check that the function evaluation value is not within the range
        """

        def test_function(n):
            return float(n)

        self.assertEqual(find(test_function, 15, 0, 10), -1)

    def test_mpmath_function(self):
        def test_function(n):
            return 0. if n <= 0 else float(zetazero(n).imag)

        y = test_function(123456789)
        z = y + 1e-8

        self.assertEqual(find(test_function, y, 0, 10000000000), 123456789)
        self.assertEqual(find(test_function, z, 0, 10000000000), -1)

    def test_single_element_range_value_present(self):
        """
        Check that the function evaluation value is within a range of a single value [a, a]
        """

        def test_function(n):
            return float(n)

        self.assertEqual(find(test_function, 3, 3, 3), 3)

    def test_single_element_range_value_not_present(self):
        """
        Check that the function evaluation value is not within a range of a single value [a, a]
        """

        def test_function(n):
            return float(n)

        self.assertEqual(find(test_function, 2, 3, 3), -1)

    def test_wrong_range(self):
        """
        Check that the range specification is wrong
        """

        def test_function(n):
            return float(n)

        self.assertEqual(find(test_function, 1, 10, 5), -1)


if __name__ == '__main__':
    unittest.main()

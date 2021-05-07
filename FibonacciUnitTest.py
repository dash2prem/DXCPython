import unittest
import fibonacci

class MyTestCase(unittest.TestCase):

    def test_fibonacci_8(self):
        wanted_result = [0, 1, 1, 2, 3, 5, 8, 13]
        test_result = fibonacci.fibinacciSeries(8)
        self.assertEqual(wanted_result, test_result)

    def test_fibonacci_20(self):
        wanted_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        test_result = fibonacci.fibinacciSeries(20)
        self.assertEqual(wanted_result, test_result)

if __name__ == '__main__' : fibonacci.main()


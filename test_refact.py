import unittest

# create a function that returns true if number is odd, or false otherwise

def is_odd(number):
    if number < 0:
        return False

    return number % 2!= 0


# create a test class & use the unittest module

class TestIsOdd(unittest.TestCase):
    def test_is_odd(self):
        # test case for a positive odd number
        self.assertEqual(is_odd(5), True)
        # test case for a positive even number
        self.assertEqual(is_odd(4), False)
        # test case for zero
        self.assertEqual(is_odd(0), False)
        # test case for a negative odd number
        self.assertEqual(is_odd(-7), False)

if __name__ == '__main__':
    unittest.main()
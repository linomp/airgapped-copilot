import unittest

# create a function that returns true if number is odd, or false otherwise

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# create a test class using the unittest module
class Test(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_odd(1), True)
        self.assertEqual(is_odd(2), False)
        self.assertEqual(is_odd(3), True)


if __name__ == '__main__':
    unittest.main()


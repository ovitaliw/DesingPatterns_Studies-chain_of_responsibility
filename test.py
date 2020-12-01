import contextlib
import unittest
from io import StringIO

import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz(self):
        list_size = 15
        expected_output = '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz'
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            fizzbuzz.fizz_buzz(list(range(1, list_size + 1)))
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()

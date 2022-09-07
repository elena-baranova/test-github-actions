import unittest
from src.greetings import say_hello

class TestGreetings(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello(), 'Hello')

if __name__ == '__main__':
    unittest.main()
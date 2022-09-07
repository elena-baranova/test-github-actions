"""This is for checking github action for tests"""
import unittest
from src.greetings import say_hello, say_welcome

class TestGreetings(unittest.TestCase):
    """Test class"""

    def test_say_hello(self):
        """Let's check if say_hello actually say Hello"""
        self.assertEqual(say_hello(), 'Hello1')

    def test_say_welcome(self):
        """Let's check if say_welcome actually say Welcome"""
        self.assertEqual(say_welcome(), 'Welcome')

if __name__ == '__main__':
    unittest.main()

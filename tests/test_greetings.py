"""This is for checking github action for tests"""
import unittest
from src.greetings import say_hello

class TestGreetings(unittest.TestCase):
    """Test class"""

    def test_say_hello(self):
        """Let's check if say_hello actually say Hello"""
        self.assertEqual(say_hello(), 'Popo')

if __name__ == '__main__':
    unittest.main()

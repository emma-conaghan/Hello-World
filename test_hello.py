import unittest
from hello import say_hello

class TestSayHello(unittest.TestCase):
    def test_default_greeting(self):
        """Test that the default greeting returns 'Hello, World!'"""
        self.assertEqual(say_hello(), "Hello, World!")

    def test_custom_name_greeting(self):
        """Test that it greets a specific name correctly"""
        self.assertEqual(say_hello("Emma"), "Hello, Emma!")

if __name__ == "__main__":
    unittest.main()

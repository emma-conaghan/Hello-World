import unittest
from hello import say_hello

class TestSayHello(unittest.TestCase):
    def test_default_greeting(self):
        """Test that the default greeting returns 'Hello, World!'"""
        self.assertEqual(say_hello(), "Hello, World!")

    def test_custom_name_greeting(self):
        """Test that it greets a specific name correctly"""
        self.assertEqual(say_hello("Emma"), "Hello, Emma!")

    def test_name_with_whitespace(self):
        """Test that leading/trailing spaces are handled correctly"""
        self.assertEqual(say_hello("  Emma  "), "Hello, Emma!")

    def test_empty_string_name(self):
        """Test that an empty string defaults to 'World'"""
        self.assertEqual(say_hello(""), "Hello, World!")

    def test_non_string_input(self):
        """Test that non-string input raises a TypeError"""
        with self.assertRaises(TypeError):
            say_hello(123)

if __name__ == "__main__":
    unittest.main()

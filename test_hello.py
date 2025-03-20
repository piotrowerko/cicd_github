import unittest
from main import greet

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World2!", "Powitanie nie jest zgodne z oczekiwaniem")

if __name__ == '__main__':
    unittest.main()
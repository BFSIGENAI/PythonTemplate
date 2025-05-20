# tests/test_module1.py
import unittest
from src.my_package import module

class TestModule(unittest.TestCase):
    def test_function(self):
        self.assertEqual(module.function(), expected_result)

if __name__ == '__main__':
    unittest.main()

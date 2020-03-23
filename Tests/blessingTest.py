import unittest
from blessing import Blessing


class MyTestCase(unittest.TestCase):
    b = Blessing("Test", giver="Test2")
    b.power = "weak"
    b.effect = "Nothing"

    def test_something(self):
        b = self.b
        self.assertEqual(b.title, "Test")
        self.assertEqual(b.given_by, "Test2")
        self.assertEqual(b.power, "weak")
        self.assertEqual(b.effect, "Nothing")


if __name__ == '__main__':
    unittest.main()

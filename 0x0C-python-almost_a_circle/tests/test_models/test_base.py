import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):

    def test_not_none(self):
        self.assertEqual(Base(12).id, 12)

    def test_none(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

if __name__ == '__main__':
    unittest.main()

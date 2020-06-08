import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).width, 10)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).height, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).x, 0)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).y, 0)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_two_input(self):
        self.assertEqual(Rectangle(10, 2).width, 10)
        self.assertEqual(Rectangle(10, 3).height, 3)
        self.assertEqual(Rectangle(10, 2).x, 0)
        self.assertEqual(Rectangle(10, 2).y, 0)
        self.assertEqual(Rectangle(10, 2).id, 10)

    def test_input(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
    
if __name__ == '__main__':
    unittest.main()

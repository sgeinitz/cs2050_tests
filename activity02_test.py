import unittest
from activity02 import Shape, Square, Triangle, Rhombus


class TestActivity02(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity02.py classes """

    def setUp(self):
        """ Define a few instances of shapes that will be used mult times. """
        self.sq = Square(5)
        self.tr = Triangle(5)
        self.rh = Rhombus(5, 87)

    def testSquareSpecs(self):
        """ Check that Square specs are derived and updated properly. """
        self.assertEqual(20, self.sq.getPerimeter())
        self.assertEqual(25, self.sq.getArea())
        self.sq.setSideLength(3)
        self.assertEqual(3, self.sq.getSideLength())
        self.assertEqual(12, self.sq.getPerimeter())
        self.assertEqual(9, self.sq.getArea())

    def testSquareIsChild(self):
        """ Confirm that Square is derived from Shape """
        self.assertTrue(issubclass(Square, Shape))

    def testTriangleSpecs(self):
        """ Check that Triangle specs are derived and updated properly. """
        self.assertEqual(15, self.tr.getPerimeter())
        self.assertAlmostEqual(10.825317547, self.tr.getArea())
        self.tr.setSideLength(3)
        self.assertEqual(3, self.tr.getSideLength())
        self.assertEqual(9, self.tr.getPerimeter())
        self.assertAlmostEqual(3.89711431702, self.tr.getArea())

    def testTriangleIsChild(self):
        """ Confirm that Triangle is derived from Shape """
        self.assertTrue(issubclass(Triangle, Shape))

    def testRhombusSpecs1(self):
        """ Check that Rhombus specs are derived and updated properly. """
        self.assertEqual(20, self.rh.getPerimeter())
        self.assertAlmostEqual(24.96573836886, self.rh.getArea())
        self.rh.setSideLength(3)
        self.assertEqual(3, self.rh.getSideLength())
        self.assertEqual(12, self.rh.getPerimeter())
        self.assertAlmostEqual(8.987665812791, self.rh.getArea())

    def testRhombusSpecs2(self):
        """ Check that Rhombus specs are same as Square for base_angle=90. """
        self.rh.setBaseAngle(90)
        self.rh.setSideLength(5.4321)
        self.sq.setSideLength(self.rh.getSideLength())
        self.assertAlmostEqual(self.sq.getArea(), self.rh.getArea())

    def testRhombusIsChild(self):
        """ Confirm that an instance of Rhombus is derived from Shape """
        self.assertTrue(issubclass(Rhombus, Shape))

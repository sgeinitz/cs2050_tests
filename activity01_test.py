import unittest
from activity01 import *


class TestActivity01Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity01.py functions """

    def testHelloWorldNormal(self):
        """ Confirm that helloWorldNormal() returns the correct string """
        expected_string = 'hello world'
        self.assertEqual(expected_string, helloWorldNormal())

    def testHelloWorldInReverse(self):
        """ Confirm that helloWorldInReverse() returns the correct string """
        expected_string = 'hello world'[::-1]
        self.assertEqual(expected_string, helloWorldInReverse())

    def testHelloWorldTimesX(self):
        """ Confirm helloWorldTimesX() returns correct string for given input """
        expected_string = 'hello world' * 3
        self.assertEqual(expected_string, helloWorldTimesX(3))

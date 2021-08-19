import unittest
from activity01 import *


class TestActivity01Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity01.py functions """

    def testHelloWorldNormal(self):
        """ Confirm that helloWorldNormal() returns the correct string """
        self.assertEqual('hello world', helloWorldNormal())

    def testHelloWorldInReverse(self):
        """ Confirm that helloWorldInReverse() returns the correct string """
        self.assertEqual('hello world'[::-1], helloWorldInReverse())

    def testHelloWorldTimesX(self):
        """ Confirm helloWorldTimesX() returns correct string for given input """
        self.assertEqual('hello world' * 3, helloWorldTimesX(3))

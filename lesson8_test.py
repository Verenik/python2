import unittest
from urok8 import *

class My_Test(unittest.TestCase):

    def test_args(self):
        self.assertEquals(adder(2, 2), 4)

    def test_erags(self):
        self.assertEquals(adder(2, 2, 'h'), 4)
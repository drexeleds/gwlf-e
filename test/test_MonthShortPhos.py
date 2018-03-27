import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import MonthShortPhos


class TestMonthShortPhos(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_MonthShortPhos(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            MonthShortPhos.MonthShortPhos_2(),
            MonthShortPhos.MonthShortPhos(), decimal=7)
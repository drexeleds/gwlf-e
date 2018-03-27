import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import MonthDischargePhos


class TestMonthDischargePhos(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_MonthDischargePhos(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            MonthDischargePhos.MonthDischargePhos_2(),
            MonthDischargePhos.MonthDischargePhos(), decimal=7)
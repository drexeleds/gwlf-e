import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.BMPs.AgAnimal import NAWMSP


class TestNAWMSP(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_NAWMSP(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSP.NAWMSP_2(),
            NAWMSP.NAWMSP(), decimal=7)
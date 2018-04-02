import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import QrunP, gwlfe


class TestQrunP(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_QrunP(self):
        z = self.z
        _, z = gwlfe.run(z)
        np.testing.assert_array_almost_equal(
            z.QrunPStorage,
            z.QrunP_isolate, decimal=7)


    # def test_QrunP2(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         QrunP.QrunP_2(),
    #         QrunP.QrunP(), decimal=7)
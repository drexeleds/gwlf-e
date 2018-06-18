import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import CNI


class TestCNI(VariableUnitTest):

    def test_CNI(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNI.CNI_f(z.NRur, z.NUrb, z.CNI_0),
            CNI.CNI(z.NRur, z.NUrb, z.CNI_0), decimal=7)

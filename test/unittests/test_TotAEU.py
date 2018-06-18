import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import TotAEU


class TestTotAEU(VariableUnitTest):

    # @skip("not ready")
    def test_TotAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotAEU.TotAEU_f(z.NumAnimals, z.AvgAnimalWt),
            TotAEU.TotAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)

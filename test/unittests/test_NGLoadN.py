import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGLoadN
from gwlfe.enums import YesOrNo


class TestNGLoadN(VariableUnitTest):

    def test_NGLoadN(self):
        z = self.z
        grazing_mask = np.where(z.GrazingAnimal_0 == YesOrNo.NO)
        np.testing.assert_array_almost_equal(
            NGLoadN.NGLoadN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            NGLoadN.NGLoadN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[grazing_mask], decimal=7)

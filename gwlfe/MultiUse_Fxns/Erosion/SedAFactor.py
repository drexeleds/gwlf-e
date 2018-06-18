from gwlfe.Input.Animals.AEU import AEU
from gwlfe.MultiUse_Fxns.Runoff.AvCN import AvCN
from gwlfe.Memoization import memoize
from gwlfe.Input.LandUse.Urb.PcntUrbanArea import PcntUrbanArea


@memoize
def SedAFactor(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF, AvSlope,
               SedAAdjust):
    result = SedAFactor_0
    pcnturbanarea = PcntUrbanArea(NRur, NUrb, Area)
    aeu = AEU(NumAnimals, AvgAnimalWt, NRur, NUrb, Area)
    avcn = AvCN(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area)
    # Recalculate Sed A Factor using updated AEU value based on animal data
    result = ((0.00467 * pcnturbanarea) +
              (0.000863 * aeu) +
              (0.000001 * avcn) +
              (0.000425 * AvKF) +
              (0.000001 * AvSlope) - 0.000036) * SedAAdjust

    if result < 0.00001:
        result = 0.00001
    return result

# @time_function #vectorization wasn't any faster
# def SedAFactor_f(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF, AvSlope,
#                SedAAdjust):
#     pcnturbanarea = PcntUrbanArea_f(NRur, NUrb, Area)
#     aeu = AEU_f(NumAnimals, AvgAnimalWt, NRur, NUrb, Area)
#     avcn = AvCN(NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area)
#     return max(((0.00467 * pcnturbanarea) +
#               (0.000863 * aeu) +
#               (0.000001 * avcn) +
#               (0.000425 * AvKF) +
#               (0.000001 * AvSlope) - 0.000036) * SedAAdjust,0.00001)
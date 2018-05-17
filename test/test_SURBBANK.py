import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import SURBBANK


class TestSURBBANK(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_SURBBANK(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SURBBANK.SURBBANK_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                                z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                z.SatStor_0, z.RecessionCoef, z.SeepCoef
                                , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow,
                                z.StreamWithdrawal, z.GroundWithdrawal
                                , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope,
                                z.SedAAdjust, z.StreamLength
                                , z.UrbBankStab, z.n42b, z.n85d),
            SURBBANK.SURBBANK(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                              z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                              z.RecessionCoef, z.SeepCoef
                              , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow,
                              z.StreamWithdrawal, z.GroundWithdrawal
                              , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope,
                              z.SedAAdjust, z.StreamLength
                              , z.UrbBankStab, z.n42b, z.n85d), decimal=7)
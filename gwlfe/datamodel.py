# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import json

import numpy as np


class DataModel(object):
    def __init__(self, data):
        self.__dict__.update(self.defaults())
        self.__dict__.update(data)

    def defaults(self):
        return {
            'AnimalFlag': 0,
            'AvGRStreamFC': 0,
            'AvGRStreamN': 0,
            'AvGRStreamP': 0,
            'AvTileDrain': np.zeros(100),
            'RurAreaTotal': 0,
            'UrbAreaTotal': 0,
            'Month': np.zeros(12),
            'Landuse': np.zeros(16),
            'Imper': np.zeros(16),
            'LoadRateImp': np.zeros((16, 3)),
            'LoadRatePerv': np.zeros((16, 3)),
            'DisFract': np.zeros((16, 3)),
            'UrbBMPRed': np.zeros((16, 3)),
            'TotSusSolids': np.zeros((16)),
            'Contaminant': np.zeros(3),
            'DayHrs': np.zeros(12),
            'Grow': np.zeros(12),
            'KV': np.zeros(12),
            'd': np.zeros(12),
            'KVD': np.zeros(12),
            'CV': np.zeros(12),
            'Acoef': np.zeros(12),
            'Area': np.zeros(16),
            'AreaE': np.zeros(16),
            'KLSCP': np.zeros(16),
            'CN': np.zeros(16),
            'KF': np.zeros(16),
            'LS': np.zeros(16),
            'C': np.zeros(16),
            'P': np.zeros(16),
            'NewCN': np.zeros((12, 16)),
            'AntMoist': np.zeros(5),
            'PcntET': np.zeros(12),
            'StreetSweepNo': np.zeros(12),
            'ISRR': np.zeros(6),
            'ISRA': np.zeros(6),
            'NitrConc': np.zeros(16),
            'PhosConc': np.zeros(16),
            'ManNitr': np.zeros(16),
            'ManPhos': np.zeros(16),
            'UrbanNitr': np.zeros(16),
            'UrbanPhos': np.zeros(16),
            'PointNitr': np.zeros(12),
            'PointPhos': np.zeros(12),
            'PointFlow': np.zeros(12),
            'AvStreamFlow': np.zeros(12),
            'AvPrecipitation': np.zeros(12),
            'AvEvapoTrans': np.zeros(12),
            'AvGroundWater': np.zeros(12),
            'AvRunoff': np.zeros(12),
            'AvErosion': np.zeros(12),
            'AvSedYield': np.zeros(12),
            'AFON': np.zeros(12),
            'AFOP': np.zeros(12),
            'AvLoad': np.zeros((12, 3)),
            'AvLuLoad': np.zeros((16, 3)),
            'UrbSedLoad': np.zeros((16, 12)),
            'AvGroundNitr': np.zeros(12),
            'AvGroundPhos': np.zeros(12),
            'AvDisNitr': np.zeros(12),
            'AvTotNitr': np.zeros(12),
            'AvDisPhos': np.zeros(12),
            'AvTotPhos': np.zeros(12),
            'AvLuRunoff': np.zeros(16),
            'AvLuErosion': np.zeros(16),
            'AvLuSedYield': np.zeros(16),
            'AvLuDisNitr': np.zeros(16),
            'AvLuTotNitr': np.zeros(16),
            'AvLuDisPhos': np.zeros(16),
            'AvLuTotPhos': np.zeros(16),
            'BSed': np.zeros(16),
            'UrbanSed': np.zeros(16),
            'UrbanErosion': np.zeros(16),
            'ErosWashoff': np.zeros((16, 12)),
            'QRunoff': np.zeros((16, 12)),
            'AgQRunoff': np.zeros((16, 12)),
            'RurQRunoff': np.zeros((16, 12)),
            'UrbQRunoff': np.zeros((16, 12)),
            'NumPondSys': np.zeros(12),
            'NumNormalSys': np.zeros(12),
            'NumShortSys': np.zeros(12),
            'NumDischargeSys': np.zeros(12),
            'NumSewerSys': np.zeros(12),
            'DailyLoad': np.zeros((50, 12, 31)),
            'SepticsDay': np.zeros(12),
            'MonthlyLoad': np.zeros((12, 31)),

            # Declare the daily values as ReDimensional arrays in
            # to Pesticide components
            'DayPondNitr': np.zeros((12, 31)),
            'DayPondPhos': np.zeros((12, 31)),
            'DayNormNitr': np.zeros((12, 31)),
            'DayNormPhos': np.zeros((12, 31)),
            'WashImperv': np.zeros(16),
            'NetSolidLoad': np.zeros(3),
            'DayShortNitr': np.zeros((12, 31)),
            'DayShortPhos': np.zeros((12, 31)),
            'DayDischargeNitr': np.zeros((12, 31)),
            'DayDischargePhos': np.zeros((12, 31)),
            'DaysYear': np.zeros(40),
            'PestAppMonth1': np.zeros(16),
            'PestAppYear1': np.zeros(16),
            'PestAppDate1': np.zeros(16),
            'PestAppMonth2': np.zeros(16),
            'PestAppYear2': np.zeros(16),
            'PestAppDate2': np.zeros(16),
            'PestShedName': np.zeros(12),
            'PestCropArea': np.zeros(12),
            'PestSoilBd': np.zeros(12),
            'PestSoilAwc': np.zeros(12),
            'PestSoilOm': np.zeros(12),
            'PestCropName': np.zeros(12),
            'PestName1': np.zeros(16),
            'PestRate1': np.zeros(31),
            'PestParamCarbon1': np.zeros(16),
            'PestParamWater1': np.zeros(16),
            'PestDecay1': np.zeros(16),
            'PestHalfLife1': np.zeros(16),
            'PestName2': np.zeros(16),
            'PestRate2': np.zeros(31),
            'PestParamCarbon2': np.zeros(16),
            'PestParamWater2': np.zeros(16),
            'PestDecay2': np.zeros(16),
            'PestHalfLife2': np.zeros(16),
            'AvStreamBankEros': np.zeros(12),
            'AvStreamBankN': np.zeros(12),
            'AvStreamBankP': np.zeros(12),
            'CropPercent': np.zeros(12),
            'PestSoilAwcCm': np.zeros(12),

            # Tile Drainage and Flow Variables
            'vTileDrain': np.zeros(12),
            'StreamWithdrawal': np.zeros(12),
            'GroundWithdrawal': np.zeros(12),
            'AvWithdrawal': np.zeros(12),
            'AvTileDrainN': np.zeros(12),
            'AvTileDrainP': np.zeros(12),
            'AvTileDrainSed': np.zeros(12),
            'AvPtSrcFlow': np.zeros(12),

            # DIMENSION LOCAL SEPTIC SYSTEM MODEL ARRAYS
            'MonthPondNitr': np.zeros(12),
            'MonthPondPhos': np.zeros(12),
            'MonthNormNitr': np.zeros(12),
            'MonthShortNitr': np.zeros(12),
            'MonthShortPhos': np.zeros(12),
            'MonthDischargeNitr': np.zeros(12),
            'MonthDischargePhos': np.zeros(12),

            # ANIMAL FEEDING OPERATIONS VARIABLES
            'AnimalName': np.zeros(9),
            'NumAnimals': np.zeros(9),
            'GrazingAnimal': np.zeros(9),
            'AnimalDailyN': np.zeros(9),
            'AnimalDailyP': np.zeros(9),
            'FCOrgsPerDay': np.zeros(9),
            'AvgAnimalWt': np.zeros(9),

            'Month': np.zeros(12),
            'NGPctManApp': np.zeros(12),
            'NGAppNRate': np.zeros(12),
            'NGAppPRate': np.zeros(12),
            'NGAppFCRate': np.zeros(12),
            'NGPctSoilIncRate': np.zeros(12),
            'NGBarnNRate': np.zeros(12),
            'NGBarnPRate': np.zeros(12),
            'NGBarnFCRate': np.zeros(12),

            'PctGrazing': np.zeros(12),
            'PctStreams': np.zeros(12),
            'GrazingNRate': np.zeros(12),
            'GrazingPRate': np.zeros(12),
            'GrazingFCRate': np.zeros(12),
            'GRPctManApp': np.zeros(12),
            'GRAppNRate': np.zeros(12),
            'GRAppPRate': np.zeros(12),
            'GRAppFCRate': np.zeros(12),
            'GRPctSoilIncRate': np.zeros(12),
            'GRBarnNRate': np.zeros(12),
            'GRBarnPRate': np.zeros(12),
            'GRBarnFCRate': np.zeros(12),

            # Calculated Values for Animal Feeding Operations
            'NGLoadN': np.zeros(9),
            'NGLoadP': np.zeros(9),
            'NGLoadFC': np.zeros(9),
            'NGAccManAppN': np.zeros(12),
            'NGAccManAppP': np.zeros(12),
            'NGAccManAppFC': np.zeros(12),
            'NGAppManN': np.zeros(12),
            'NGInitBarnN': np.zeros(12),
            'NGAppManP': np.zeros(12),
            'NGInitBarnP': np.zeros(12),
            'NGAppManFC': np.zeros(12),
            'NGInitBarnFC': np.zeros(12),

            'GRLoadN': np.zeros(9),
            'GRLoadP': np.zeros(9),
            'GRLoadFC': np.zeros(9),
            'GRAccManAppN': np.zeros(12),
            'GRAccManAppP': np.zeros(12),
            'GRAccManAppFC': np.zeros(12),
            'GRAppManN': np.zeros(12),
            'GRInitBarnN': np.zeros(12),
            'GRAppManP': np.zeros(12),
            'GRInitBarnP': np.zeros(12),
            'GRAppManFC': np.zeros(12),
            'GRInitBarnFC': np.zeros(12),
            'GrazingN': np.zeros(12),
            'GrazingP': np.zeros(12),
            'GrazingFC': np.zeros(12),
            'GRStreamN': np.zeros(12),
            'GRStreamP': np.zeros(12),
            'GRStreamFC': np.zeros(12),
            'AvAnimalN': np.zeros(12),
            'AvAnimalP': np.zeros(12),
            'AvAnimalFC': np.zeros(12),
            'AvWWOrgs': np.zeros(12),
            'AvSSOrgs': np.zeros(12),
            'AvUrbOrgs': np.zeros(12),
            'AvWildOrgs': np.zeros(12),
            'AvTotalOrgs': np.zeros(12),
            'AvCMStream': np.zeros(12),
            'AvOrgConc': np.zeros(12),
            'AvGRLostBarnN': np.zeros(12),
            'AvGRLostBarnP': np.zeros(12),
            'AvNGLostBarnN': np.zeros(12),
            'AvNGLostBarnP': np.zeros(12),
            'AvNGLostManP': np.zeros(12),
            'AvNGLostBarnFC': np.zeros(12),
            'AvGRLostBarnFC': np.zeros(12),

            # Initialize non-arrayed variables
            'Nqual': 0,
            'q': 0,
            'k': 0,
            'BasinArea': 0,
            'Qretention': 0,
            'FilterEff': 0,
            'FilterWidth': 0,
            'OutFiltWidth': 0,
            'Capacity': 0,
            'BasinDeadStorage': 0,
            'DaysToDrain': 0,
            'CleanMon': 0,
            'Clean': 0,
            'CleanSwitch': 0,
            'OutletCoef': 0,
            'BasinVol': 0,
            'Volume': 0,
            'ActiveVol': 0,
            'DetentFlow': 0,
            'AnnDayHrs': 0,
            'AreaTotal': 0,
            'SweepFrac': np.zeros(12),

            'CNI': np.zeros((3, 16)),
            'CNP': np.zeros((3, 16)),

            # Load Delivery data
            'AttenFlowDist': 0,
            'AttenFlowVel': 0,
            'AttenLossRateN': 0,
            'AttenLossRateP': 0,
            'AttenLossRateTSS': 0,
            'AttenLossRatePath': 0,
            'StreamFlowVolAdj': 1,
        }

    def __str__(self):
        return '<GWLF-E DataModel>'

    def tojson(self):
        return json.dumps(self.__dict__, cls=NumpyAwareJSONEncoder)


class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

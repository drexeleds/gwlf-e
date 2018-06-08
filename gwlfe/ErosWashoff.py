import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU_function import NLU_function
from Water import Water
from RurEros import RurEros
from RurEros import RurEros_2


@memoize
def ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS, C, P, Area):
    result = np.zeros((NYrs, 16, 12))
    nlu = NLU_function(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rureros = RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][l][i] = result[Y][l][i] + rureros[Y][i][j][l]
                else:
                    pass
    return result

@memoize
def ErosWashoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS, C, P, Area):
    return np.sum(RurEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area), axis=2)

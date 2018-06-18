from numpy import zeros

# from Timer import time_function
from Melt_1 import Melt_1, Melt_1_f
from Memoization import memoize
from Rain import Rain, Rain_f


@memoize
def Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = zeros((NYrs, 12, 31))
    melt_1 = Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rain = Rain(NYrs, DaysMonth, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = rain[Y][i][j] + melt_1[Y][i][j]
    return result

@memoize
def Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    melt_1 = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rain = Rain_f(Temp, Prec)
    return rain + melt_1
import numpy as np
from Timer import time_function
from NLU import NLU
from numba import jit
from Memoization import memoize


@memoize
def NewCN(NRur, NUrb, CN):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((3, nlu))
    for l in range(NRur):
        result[0][l] = CN[l] / (2.334 - 0.01334 * CN[l])
        result[2][l] = CN[l] / (0.4036 + 0.0059 * CN[l])
        if result[2][l] > 100:
            result[2][l] = 100
    return result

# @time_function
# @jit(cache=True, nopython = True)
@memoize
def NewCN_2(NRur, NUrb, CN):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((3, nlu))
    result[0,:] = CN / (2.334 - 0.01334 * CN)
    result[2,:] = CN / (0.4036 + 0.0059 * CN)
    result[2,:][np.where(result[2,:]>100)] = 100
    return result
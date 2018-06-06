import numpy as np
from gwlfe.Timer import time_function
from InitGrN import InitGrN
from InitGrN import InitGrN_2


def GRAppManN(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    result = np.zeros((12,))
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = GRPctManApp[i] * init_gr_n
    return result


def GRAppManN_2(GRPctManApp, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN):
    init_gr_n = InitGrN_2(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    return GRPctManApp * init_gr_n
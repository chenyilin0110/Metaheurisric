import numpy as np
import random

def initial(data, city):
    solution = np.zeros((city, 3))
    for eachcity in range(city):
        r = random.randint(0, len(data)-1)
        for eachdim in range(np.size(data,1)):
            solution[eachcity][eachdim] = data[r][eachdim]
        data = np.delete(data, r, 0)
    return solution

def initial_sa(bit):

    return 0
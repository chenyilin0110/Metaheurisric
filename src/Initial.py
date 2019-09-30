import numpy as np
import random

def initial(data, city, dim):
    dim += 1 #point_number, x, y
    solution = np.zeros((city, dim))
    for eachcity in range(city):
        r = random.randint(0, len(data)-1)
        for eachdim in range(np.size(data,1)):
            solution[eachcity][eachdim] = data[r][eachdim]
        data = np.delete(data, r, 0)
    return solution
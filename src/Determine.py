import numpy as np

def determine(solution):
    distance = 0
    for eachcity in range(np.size(solution, 0)):
        if eachcity < (np.size(solution, 0) - 1):
            x1 = solution[eachcity][1]
            x2 = solution[eachcity+1][1]
            y1 = solution[eachcity][2]
            y2 = solution[eachcity+1][2]
        else:
            x1 = solution[eachcity][1]
            x2 = solution[0][1]
            y1 = solution[eachcity][2]
            y2 = solution[0][2]
        distance += np.sqrt(np.square(x1-x2) + np.square(y1-y2))
    return distance
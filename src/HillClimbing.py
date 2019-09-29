import numpy as np
import sys
from Initial import initial
from Transaction import transaction
from Determine import determine
from Evaluation import evaluation

iteration = sys.argv[1]
city = sys.argv[2]

best_value = 0
eachiteration = 0

data = np.loadtxt('dataSet/' + city + '.txt', dtype=np.str, delimiter=" ")

solution = initial(data, int(city))

while(eachiteration != int(iteration)):
    old_solution,  solution = transaction(solution)

    distance = determine(solution)

    if eachiteration == 0:
        best_value = distance
    else:
        old_distance = determine(old_solution)
        best_value, solution = evaluation(old_solution, old_distance, solution, distance)
    
    print(eachiteration + 1, best_value)
    
    eachiteration += 1
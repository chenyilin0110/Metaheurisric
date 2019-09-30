import numpy as np
import sys
from Initial import initial
from Transaction import transaction
from Evaluation import evaluation
from Determine import determine

iteration = sys.argv[1]
city = sys.argv[2]
dim = sys.argv[3]

best_value = 0
eachiteration = 0

data = np.loadtxt('dataSet/' + city + '.txt', dtype=np.str, delimiter=" ")

solution = initial(data, int(city), int(dim))
best_solution = solution.copy()
best_value = evaluation(solution)

while(eachiteration != int(iteration)):
    old_solution,  solution = transaction(solution)

    distance = evaluation(solution)
    
    best_value, best_solution = determine(best_solution, best_value, solution, distance)
    
    solution = best_solution.copy()
    
    print(eachiteration + 1, best_value)
    
    eachiteration += 1
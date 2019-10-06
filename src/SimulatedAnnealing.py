import numpy as np
import sys
import math
from Initial import initial
from Transaction import transaction
from Evaluation import evaluation
from Determine import determine_sa

iteration = sys.argv[1]
city = sys.argv[2]
dim = sys.argv[3]
neighbor_number = sys.argv[4]
temperature = sys.argv[5]
rate = sys.argv[6]

best_value = 0
eachiteration = 0
solution = []

data = np.loadtxt('dataSet/' + city + '.txt', dtype=np.str, delimiter=" ")

temp = initial(data, int(city), int(dim))

for each_neighbor_number in range(int(neighbor_number)):
    solution.append(temp)

solution = np.asarray(solution)
old_solution = solution.copy()

best_solution = solution[0].copy()
best_value = evaluation(solution[0])

while((eachiteration != int(iteration)) and (float(temperature) > 0)):
    distance = np.zeros(int(neighbor_number))
    
    for each_neighbor_number in range(int(neighbor_number)):
        old_solution[each_neighbor_number],  solution[each_neighbor_number]\
             = transaction(solution[each_neighbor_number])
        distance[each_neighbor_number] = evaluation(solution[each_neighbor_number])

    best_neighbor_distance = np.min(distance)
    best_neighbor_distance_index = np.where(distance==np.min(distance))
    
    # the best neighbor has more than one
    if np.size(best_neighbor_distance_index,1) > 1:
        best_neighbor_distance_index = best_neighbor_distance_index[0][0]
        best_neighbor_distance = distance[best_neighbor_distance_index]

    try:
        exp_change = math.exp(\
        (-1) * (best_neighbor_distance - best_value)/float(temperature))
    except OverflowError:
        exp_change = float('inf')

    temp_value, temp_solution= determine_sa\
        (best_solution, best_value, solution[best_neighbor_distance_index], best_neighbor_distance, exp_change)

    best_value = temp_value
    best_solution = temp_solution

    for each_neighbor_number in range(int(neighbor_number)):
        solution[each_neighbor_number] = best_solution.copy()

    temperature = float(rate) * float(temperature)
    
    print(best_value)
    
    eachiteration += 1
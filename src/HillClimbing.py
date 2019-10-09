import numpy as np
import sys
from Initial import initial
from Transaction import transaction
from Evaluation import evaluation
from Determine import determine
import matplotlib.pyplot as plt

iteration = sys.argv[1]
city = sys.argv[2]
dim = sys.argv[3]

best_value = 0
eachiteration = 0

data = np.loadtxt('dataSet/' + city + '.txt', dtype=np.str, delimiter=" ")

solution = initial(data, int(city), int(dim))
best_solution = solution.copy()
best_value = evaluation(solution)

plt.figure()
plt.ion()

while(eachiteration != int(iteration)):
    old_solution,  solution = transaction(solution)

    distance = evaluation(solution)
    
    best_value, best_solution = determine(best_solution, best_value, solution, distance)
    
    solution = best_solution.copy()
    
    print(best_value)
    
    eachiteration += 1

    x = []
    y = []
    for each_city in range(int(city)):
        x.append(best_solution[each_city][1])
        y.append(best_solution[each_city][2])
    x.append(best_solution[0][1])
    y.append(best_solution[0][2])
    
    plt.cla()
    plt.title('Hill Climbing' + ' ' + str(eachiteration) + ' ' + str(best_value))
    plt.plot(x, y, 'r')
    plt.pause(0.05)
plt.ioff()
plt.show()
plt.close()
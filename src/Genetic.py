import numpy as np
import sys
import math
import random
import operator
from Initial import initial
from Tournament import select_tournament
from Transaction import transaction
from Evaluation import evaluation
from Determine import determine_sa
import Update
from Plot import plot_sa
import matplotlib.pyplot as plt

# iteration = sys.argv[1]
# city = sys.argv[2]
# dim = sys.argv[3]
# chromosome = sys.argv[4]
# crossover_probability = sys.argv[5]
# mutation_probability = sys.argv[6]
# tournament = sys.argv[7]
iteration = 1
city = "51"
dim = 2
chromosome = 10
crossover_probability = 0.8
mutation_probability = 1
tournament = 7

best_value = 0
eachiteration = 0
solution = []

data = np.loadtxt('dataSet/' + city + '.txt', dtype=np.str, delimiter=" ")

for each_chromosome in range(int(chromosome)):
    solution.append(initial(data, int(city), int(dim)))


solution = np.asarray(solution)
old_solution = solution.copy()

best_solution = solution[0].copy()
best_value = evaluation(solution[0])

plt.figure()
plt.ion()

while(eachiteration != int(iteration)):

    for each_chromosome in range(int(chromosome)):
        solution[each_chromosome] = select_tournament(int(tournament), chromosome, solution, old_solution)


    eachiteration += 1

plt.ioff()
plt.show()
plt.close()
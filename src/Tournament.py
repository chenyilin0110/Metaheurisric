import numpy as np
import random
from Evaluation import evaluation

def select_tournament(tournament, chromosome, solution, old_solution):
    tournament_index = []
    tournament_distance = []
    for i in range(int(tournament)):
        r = random.randint(0,chromosome-1)
        tournament_index.append(r)
        tournament_distance.append(evaluation(solution[r]))
    # tournament_best_value = np.min(tournament_distance)
    tournament_best_index = np.where(tournament_distance==np.min(tournament_distance))
    
    # the best tournament has more than one
    if np.size(tournament_best_index,1) > 1:
        tournament_best_index = tournament_best_index[0][0]
        tournament_distance = tournament_distance[tournament_best_index]

    return old_solution[tournament_index[tournament_best_index]]
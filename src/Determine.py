import random

def determine(old_solution, old_distance, new_solution, new_distance):
    if new_distance < old_distance:
        return new_distance, new_solution
    else:
        return old_distance, old_solution

def determine_sa(old_solution, old_distance, new_solution, new_distance, exp_change):
    r = random.random()
    
    if (new_distance < old_distance) or (exp_change > r):
        return new_distance, new_solution
    else:
        return old_distance, old_solution
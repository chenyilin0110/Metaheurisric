import random

def transaction(solution):
    new_solution = solution.copy()
    r1 = random.randint(0, len(solution)-1)
    flag = 1
    
    while(flag):
        r2 = random.randint(0,len(solution)-1)
        if r2 != r1:
            flag = 0
    
    # change two point
    temp = new_solution[r1].copy()
    new_solution[r1] = solution[r2]
    new_solution[r2] = temp
    
    return solution, new_solution
def update_neighbor_solution(neighbor_number, best_solution, solution):
    for each_neighbor_number in range(neighbor_number):
        solution[each_neighbor_number] = best_solution.copy()
    return solution
def update_temperature(rate, temperature):
    temperature = float(rate) * float(temperature)
    return temperature
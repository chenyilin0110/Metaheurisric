def evaluation(old_solution, old_distance, new_solution, new_distance):
    if new_distance < old_distance:
        return new_distance, new_solution
    else:
        return old_distance, old_solution
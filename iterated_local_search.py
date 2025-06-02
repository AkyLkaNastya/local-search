import time
from laba_functions import *

def iterated_local_search(data_size, distance_matrix, flow_matrix, k=5, max_iterations=100, ls_max_iterations=1000):
    initial_sol = initial_solution(data_size)
    initial_target = calculate_target(initial_sol, distance_matrix, flow_matrix)
    
    current_solution, current_target = local_search_best_improvement(initial_sol, initial_target, data_size, distance_matrix, flow_matrix, ls_max_iterations)
    
    best_solution = current_solution.copy()
    best_target = current_target
    
    for i in range(max_iterations):
        p_solution = perturbation(current_solution, k)
        p_target = calculate_target(p_solution, distance_matrix, flow_matrix)
        
        new_solution, new_target = local_search_best_improvement(p_solution, p_target, data_size, distance_matrix, flow_matrix, ls_max_iterations)

        if new_target < current_target:
            current_solution, current_target = new_solution, new_target
        
        if current_target < best_target:
            best_solution = current_solution.copy()
            best_target = current_target
    
    return best_solution, best_target

data = ["ai20a", "ai40a", "ai60a", "ai80a", "ai100a"]

for i in range(len(data)):
    print("\n============", 't' + data[i], "============")

    start = time.time()

    data_size, distance_matrix, flow_matrix = file_reader('t'+ data[i])
    best_solution, best_target = iterated_local_search(data_size, distance_matrix, flow_matrix)

    end = time.time()

    print("\nBest solution found:", best_solution)
    print("Best target:", best_target)
    print(f'Time: {(end-start):.4f}')

    name = 'T' + data[i]
    with open(f'ils_results/{name}.sol', 'w') as file:
        file.write(' '.join(map(str, best_solution)))
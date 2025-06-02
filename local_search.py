import time
from laba_functions import *

data = ["ai20a", "ai40a", "ai60a", "ai80a", "ai100a"]

for i in range(len(data)):
    print("\n============", 't' + data[i], "============")

    start = time.time()

    data_size, distance_matrix, flow_matrix = file_reader('t'+ data[i])
    current_solution = initial_solution(data_size)
    current_target = calculate_target(current_solution, distance_matrix, flow_matrix)
    best_solution, best_target = local_search_best_improvement(current_solution, current_target, data_size, distance_matrix, flow_matrix)

    end = time.time()

    print("\nBest solution found:", best_solution)
    print("Best target:", best_target)
    print(f'Time: {(end-start):.4f}')

    name = 'T' + data[i]
    with open(f'ls_results/{name}.sol', 'w') as file:
        file.write(' '.join(map(str, best_solution)))
import random

# Функция для чтения файлов.
def file_reader(file):
    with open('files/' + file, "r") as f:
        file_data = [line.strip() for line in f if line.strip()]

    data_size = int(file_data[0])
    distance_matrix = []
    for i in range(1, data_size + 1):
        row = [int(num) for num in file_data[i].split()]
        distance_matrix.append(row)

    flow_matrix = []
    for i in range(data_size + 1, 2*data_size + 1):
        row = [int(num) for num in file_data[i].split()]
        flow_matrix.append(row)

    return data_size, distance_matrix, flow_matrix

# Функция для поиска начального решения.
def initial_solution(data_size):
    solution = list(range(data_size))
    random.shuffle(solution)  

    return solution

# Функция для вычисления целевой функции
def calculate_target(solution, distance_matrix, flow_matrix):
    target = 0
    for i in range(len(solution)):
        for j in range(len(solution)):
            target += distance_matrix[i][j] * flow_matrix[solution[i]][solution[j]]

    return target

# Функция для вычисления перестановки дельты для r-s.
def delta_calculator(current_solution, r, s, n, F, D):
    new_delta = 0
    for i in range(n):
        if (i != r) and (i != s):
            new_delta = new_delta + (F[current_solution[r]][current_solution[i]] - F[current_solution[s]][current_solution[i]])*(D[s][i] - D[r][i])
    new_delta = 2 * new_delta
    return new_delta

# local search
def local_search_best_improvement(current_solution, current_target, n, distance_matrix, flow_matrix, max_iterations=1000):

    best_solution = current_solution.copy()
    best_target = current_target
    improved = True
    iterations = 0
    
    while improved and (iterations < max_iterations):
        improved = False
        best_delta = 0
        best_swap = None
        
        for i in range(n):
            for j in range(i+1, n):
                delta = delta_calculator(best_solution, i, j, n, flow_matrix, distance_matrix)
                
                if delta < best_delta:
                    best_delta = delta
                    best_swap = (i, j)
        
        if (best_swap is not None) and (best_delta < 0):
            i, j = best_swap
            
            best_solution[i], best_solution[j] = best_solution[j], best_solution[i]
            best_target += best_delta
            improved = True
        
        iterations += 1
    
    return best_solution, best_target

# Случайная перестановка k городов
def perturbation(solution, k):
    perturbed_solution = solution.copy()

    indices = random.sample(range(len(solution)), k)
    values = [perturbed_solution[i] for i in indices]

    random.shuffle(values)

    for i, index in enumerate(indices):
        perturbed_solution[index] = values[i]

    return perturbed_solution


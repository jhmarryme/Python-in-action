def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'column':
        matrix = [list(row) for row in zip(*matrix)]
    means = []
    for row in matrix:
        means.append(sum(row) / len(row))
    return means


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix, mode))
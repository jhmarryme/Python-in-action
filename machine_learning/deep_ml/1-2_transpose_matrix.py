def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return [list(row) for row in zip(*a)]


a = [[1,2,3],[4,5,6]]

print(transpose_matrix(a))
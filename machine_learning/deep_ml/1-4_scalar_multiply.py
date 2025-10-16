def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return  [[e * scalar for e in row] for row in matrix]


matrix = [[1, 2], [3, 4]]
calar = 2
print(scalar_multiply(matrix, scalar=calar))
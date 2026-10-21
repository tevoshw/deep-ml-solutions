def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	mean = []

	if mode == 'column':
		for col in range(len(matrix[0])):
			actual_column_mean = 0
			for row in range(len(matrix)):
				actual_column_mean += matrix[row][col]
			mean.append(actual_column_mean / len(matrix))

	elif mode == 'row':
		for row in range(len(matrix)):
			actual_row_mean = 0
			for col in range(len(matrix[0])):
				actual_row_mean += matrix[row][col]
			mean.append(actual_row_mean / len(matrix[0]))

	else:
		return -1
			
	return mean
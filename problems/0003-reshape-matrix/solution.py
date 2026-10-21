import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	old_shape_x, old_shape_y = len(a), len(a[0])
	new_shape_x, new_shape_y = new_shape
	if old_shape_x * old_shape_y != new_shape_x * new_shape_y:
		return []

	flat_matrix = []
	for row in range(old_shape_x): # x
		for col in range(old_shape_y): # y
			flat_matrix.append(a[row][col])

	reshaped_matrix = []
	idx = 0
	for row in range(new_shape_x): # x'
		actual = []
		for col in range(new_shape_y): # y'
			actual.append(flat_matrix[idx])
			idx += 1
		reshaped_matrix.append(actual)

	return reshaped_matrix
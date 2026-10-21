import numpy as np

def to_categorical(x, n_col=None):
	# Your code here

	seq = x.shape[0]
	y = np.max(x) + 1

	if n_col is not None:
		y = n_col

	matrix = np.zeros((seq, y))

	for sample in range(seq):
		matrix[sample][x[sample]] = 1

	return matrix



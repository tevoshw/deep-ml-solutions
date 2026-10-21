import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here

	euler = np.exp(scores)
	sums = np.sum(euler)
	softmax = np.array(euler / sums)
	log = np.log(softmax)
	return log
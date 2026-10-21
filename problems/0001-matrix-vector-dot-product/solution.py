def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	total = []
	if len(a[0]) != len(b):
		return -1
	else:
		for row in range(len(a)):
			sums = 0
			values_a = a[row]
			values_b = b

			for x in range(len(b)):
				sums += values_a[x] * values_b[x]
			total.append(sums)	
	return total

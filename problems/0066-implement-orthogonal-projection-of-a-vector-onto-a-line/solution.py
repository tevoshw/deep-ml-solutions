
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	up = sum(x * y for x, y in zip(L, v))
	down = sum(x * y for x, y in zip(L, L))

	return [(up / down) * y for y in L]


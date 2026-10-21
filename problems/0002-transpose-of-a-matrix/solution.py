def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    matrix = []
    for col in range(len(a[0])): # 2
        actual = []
        for row in range(len(a)): # 3
            actual.append(a[row][col])
        matrix.append(actual)
    return matrix
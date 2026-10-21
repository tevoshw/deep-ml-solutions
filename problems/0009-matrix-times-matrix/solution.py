def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    c = []

    if len(a[0]) != len(b):
        return -1

    for row in range(len(a)):
        row_sum = []
        for col in range(len(b[0])):
            sums = 0
            row_a = a[row]
            for x in range(len(row_a)):
                sums += row_a[x] * b[x][col]
            row_sum.append(sums)
        c.append(row_sum)
	
    return c
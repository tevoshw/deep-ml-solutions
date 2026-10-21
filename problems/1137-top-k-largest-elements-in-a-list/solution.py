def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order

    n = len(values)

    values_sorted = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values[-3:][::-1]
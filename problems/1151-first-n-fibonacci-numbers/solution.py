def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers

    list = []


    if n == 0:
        return list
    elif n == 1:
        list.append(0)
        return list
    else:
        list.append(0)
        list.append(1)
        for x in range(n - 2): 
            next = list[-1] + list[-2]
            list.append(next)
        return list

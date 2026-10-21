import math

def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    euler = [math.exp(n - m) for n in scores]
    sums = sum(euler)
    values = [e / sums for e in euler]

    return values
    
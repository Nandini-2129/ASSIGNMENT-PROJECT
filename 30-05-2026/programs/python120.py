def compound_interest(p, t, r, n):
    a = p * (1 + (r / n)) ** (n * t)
    return round(a, 2)
print(compound_interest(1000, 2, 0.05, 4))

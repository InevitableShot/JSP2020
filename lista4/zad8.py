def sumH(n):
    s = 0.0
    for i in range(1,n+1):
        s = s + 1/i
    return s
n = 15
print(f'Suma {n} elementów szeregu harmonicznego wynosi: {sumH(n)}')
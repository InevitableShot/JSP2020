def series(n,a1=1,q=2):
    n = a1 * pow(q,n-1)
    return n
print(series(5))
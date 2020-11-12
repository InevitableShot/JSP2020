def nwd(a,b): #można użyć math.gcd
    while(b):
        a, b = b, a%b
    return a
print(f'NWD podanych liczb wynosi: {nwd(60,48)}')
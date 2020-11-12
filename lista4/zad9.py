def factorial(n): #można użyć math.factorial
    fact = 1
    if (n == 0):
         return fact
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact
print(factorial(5))
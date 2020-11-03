m = int(input("Podaj liczbe wierszy: "))
n = int(input("Podaj liczbe kolumn: "))
print(*[[i*j for i in range(0,n)] for j in range(0,m)], sep="\n")
#print(*[[[j,i] for i in range(0,n)] for j in range(0,m)], sep="\n")  #sprawdzenie 
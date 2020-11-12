from functools import reduce    #można zastosować math.prod 
tab = [x for x in range(1, 11)]
print(f'Suma  elementów tablicy wynosi: {sum(tab)}')
print(f'Iloczyn elementów tablicy wynosi: {reduce((lambda a,b: a*b), tab)}') 

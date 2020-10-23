import math

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
k = float(input('Podaj kat: '))*math.pi/180
sin = math.sin(k)
p = (a*b*sin)/2
print(p)

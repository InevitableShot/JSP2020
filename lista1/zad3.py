import math

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
k = float(input('Podaj kat: '))*math.pi/180
s = math.sin(k)
h = b/s
p = (a*h)/2
print(p)

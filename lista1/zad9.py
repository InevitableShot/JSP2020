import math
import numpy

z = complex(float(input('Podaj czesc rzeczywista liczby zespolonej: ')), float(input('Podaj czesc urojona liczby zespolonej: ')))
absolute = math.sqrt(z.real**2 + z.imag**2)
arg = numpy.angle(z, deg=True)
zz = z.conjugate()
print(z)
print(absolute)
print(arg)
print(zz)

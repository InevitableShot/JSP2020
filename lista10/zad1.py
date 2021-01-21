from math import pi


class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return pi*self.promien**2

    def obwod(self):
        return 2*pi*self.promien


kolo = Kolo(1)
print(kolo.pole())
print(kolo.obwod())

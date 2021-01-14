class Kolo:
    def __init__(self,promien):
        self.promien = promien

    def pole(self):
        from math import pi
        return pi*self.promien**2

    def obwod(self):
        from math import pi
        return 2*pi*self.promien


kolo = Kolo(1)
print(kolo.pole())
print(kolo.obwod())
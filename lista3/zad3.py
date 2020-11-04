import math 
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj wyraz wolny c: "))
delta = (b**2)-(4*a*c)
if a == 0:
    print("To nie jest funkcja kwadratowa!")
else:
    print(f"Twoja funkcja to:  {a}x^2 + {b}x + {c}")
    if delta == 0:
        print(f"x0 = {(-b)/(2*a)} ")
    elif delta < 0:
        print("Ta funkcja nie ma miejsc zerowych")
    else:
        print(f"x1 = {((-b)-(math.sqrt(delta)))/(2*a)} ")
        print(f"x2 = {((-b)+(math.sqrt(delta)))/(2*a)} ")

roman = {1000: "M", 980: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

x = int(input("Podaj liczbe calkowita: "))
print("Liczba ", str(x), " w notacji rzymskiej to: ")
r = list(roman.keys())
r.sort()
r.reverse()
print(r)
lr = ""
for i in r:
    while i <= x:
        lr += roman[i]
        x -= i
print(lr)

roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

x = int(input("Podaj liczbe calkowita: "))
r = list(roman.keys())
lr = ""
for i in r:
    while i <= x:
        lr += roman[i]
        x -= i
print(f'Liczba w notacji rzymskiej to: {lr}')
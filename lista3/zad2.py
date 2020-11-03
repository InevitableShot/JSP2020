def ver1(n):
    if (n % 2 == 0):
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")


def ver2(n):
    n_type = ["Liczba jest parzysta", "Liczba jest nieparzysta"]
    print(n_type[n % 2])


def main():
    n = int(input("Podaj liczbe calkowita: "))
    ver1(n)
    ver2(n)


main()

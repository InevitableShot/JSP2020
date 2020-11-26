from trojkat import *
def main():
    a = int(input("Podaj bok a: "))
    b = int(input("Podaj bok b: "))
    c = int(input("Podaj bok c: "))
    if (a + b <= c) or (a + c <= b) or (b + c <= a): 
        print("Nie można zbudować trójkąta")
    else:
        print(f'Obwód trójkąta wynosi: {circuit(a,b,c)}')
        print(f'Pole trójkąta wynosi: {surface_area(a,b,c)}')
        print(triangle_type(a,b,c))
        print(triangle_angle(a,b,c))

main()
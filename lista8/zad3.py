import pathlib 
import random
import sys


n = int(input("Podaj ile numerow PESEL wygenerowac: "))
path = pathlib.Path(__file__).parent.resolve()
file_path = path / 'PESEL.txt'
print(file_path)

try:
    with file_path.open(mode="w") as file:
        pesel_tab = []
        odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32,)
        even_months = (4, 6, 9, 11, 24, 26, 29, 31)
        for index in range(0,n):
            pesel = ""
            year = random.randint(1900,2099)
            if year <= 1999:
                month = random.randint(1,12)
            elif year >= 2000:
                month = random.randint(1,12) + 20
            if month in odd_months:
                day = random.randint(1,31)
            elif month in even_months:
                day = random.randint(1,30)
            else:
                if year % 4 == 0 and year != 1900:
                    day = random.randint(1,29)
                else:
                    day = random.randint(1,28)
            
            four_random = str(random.randint(1000,9999))
            y = '%02d' % (year % 100)
            m = '%02d' % month
            dd = '%02d' % day
            pesel+=y[0]+y[1]+m[0]+m[1]+dd[0]+dd[1]+four_random[0]+four_random[1]+four_random[2]+four_random[3]
            a,b,c,d,e,f,g,h,i,j = [int(char) for char in pesel]
            check = 1 * a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
            if check % 10 == 0:
                k = 0
            else:
                k = 10 - (check % 10)
            pesel+=str(k)
            pesel_tab.append(pesel)
        for item in pesel_tab:
            file.write(item + '\n')
except OSError as error:
    print(f'Błąd pliku lub systemu: {error}')
except:
    print(f'Nieprzewidziany błąd: ', sys.exc_info())
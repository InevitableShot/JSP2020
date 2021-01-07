import pathlib 
import sys


file = input("Podaj plik z numerami PESEL w formacie folder/nazwa.rozszerzenie: ")
path = pathlib.Path(__file__).parent.resolve()
file_path = path / file

try:
    with file_path.open(mode="r") as file:
        pesel_tab = [item.strip() for item in file.readlines()]
        with (path / "PESELdane.txt").open(mode="w"):
            pass
        for item in pesel_tab:
            numbers = [int(char) for char in item]
            check = 1*numbers[0] + 3*numbers[1] + 7*numbers[2] + 9*numbers[3] + 1*numbers[4] + 3*numbers[5] + 7*numbers[6] + 9*numbers[7] + 1*numbers[8] + 3*numbers[9] + 1*numbers[10]
            if check % 10 == 0:
                female = (0, 2, 4, 6, 8)
                if numbers[9] in female:
                    sex = "kobieta"
                else:
                    sex = "mężczyzna"
                day = item[4:6]
                if int(item[2:4]) <= 12:
                    month = item[2:4]
                    year = "19" + item[0:2]
                else:
                    month = int(item[2:4])-20
                    month = '%02d' % month
                    year = "20" + item[0:2]
                with (path / "PESELdane.txt").open(mode="a") as file2:
                    file2.write(f'nr PESEL: {item}\ndata urodzenia: {day}-{month}-{year}; \t płeć: {sex}\n')
except OSError as error:
    print(f'Błąd pliku lub systemu: {error}')
except:
    print(f'Nieprzewidziany błąd: ', sys.exc_info())
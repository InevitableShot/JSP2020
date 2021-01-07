from datetime import date
from SzyfrCezara import encrypt
import sys
import pathlib 


filename = input("Podaj sciezke do pliku ktory chcesz zaszyfrowac w formacie (folder/nazwa.rozszerzenie): ")
key = int(input("Podaj klucz: "))
folder = input("Podaj folder/foldery do zapisu pliku w formacie (folder/podfolder): ")
path = pathlib.Path(__file__).parent.resolve()
file_path = path / filename
folder_path = path / folder
encrypted_path = folder_path / f'plik_zaszyfrowany{key}_{date.today().strftime("%Y-%m-%d")}.txt'

try:
    with file_path.open(mode="r") as file:
        string = file.read()
        folder_path.mkdir(parents=True, exist_ok=True)
        with encrypted_path.open(mode="w") as file2:
            file2.write(encrypt(string, key))
except OSError as error:
    print(f'Błąd pliku lub systemu: {error}')
except:
    print(f'Niespodziewany błąd: ', sys.exc_info())
    
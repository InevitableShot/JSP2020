from SzyfrCezara import decrypt
import sys
import pathlib


filename = input("Podaj sciezke do pliku ktorych chcesz odszyfrowac w formacie (folder/nazwa.rozszerzenie) : ")
path = pathlib.Path(__file__).parent.resolve()
file_path = path / filename
name = file_path.name
if name[18].isdigit():
    key = int(file_path.name[17:19])
    print(key)
else:
    key = int(file_path.name[17])
name = name[17:]
name = "plik_deszyfrowany" + name
decrypted_path = file_path.parent / name

try:
    with file_path.open(mode="r") as file:
        string = file.read()
        with decrypted_path.open(mode="w") as file2:
            file2.write(decrypt(string, key))
except OSError as error:
    print(f'Błąd pliku lub systemu: {error}')
except:
    print(f'Nieprzewidziany błąd: ', sys.exc_info())
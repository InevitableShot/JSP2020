import numpy as np
import sys 

try:
    try:
        data = sys.argv[1]
    except:
        data = input()
    data = [int(item) for item in data.split(",")]
    print(f"Średnia = {np.average(data)}")
    print(f"Wariancja = {np.var(data)}")
    print(f"Odchylenie standardowe = {np.std(data)}")
except ValueError:
    print(f"Błędnie wprowadzone dane, kolejne liczby powinny być przedzielone przecinkiem.")
except:
    print(f'Wystąpił błąd: ', sys.exc_info())
    


import re
a = input("Podaj litere: ")
if re.match("[aąeęioóuy]", a):
    print(f"Litera {a} jest samogłoską")
else:
    print(f"Litera {a} jest spółgłoską")

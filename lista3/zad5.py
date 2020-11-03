import re
password = input("Podaj haslo: ")
if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[$#@]", password) and 6 <= len(password) <= 16:
    print("Twoje hasło spełnia wymagania")
else:
    print("Twoje hasło nie spełnia wymagań")

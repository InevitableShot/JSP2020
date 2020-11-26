klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
text = "to jest moj tekst"

def cypher(text):
    encrypted = ""
    for character in text:
        if character in klucz:
            encrypted += klucz[character]
        else:
            encrypted += character
    return encrypted


def decypher(encrypted):
    decrypted = ""
    for char in encrypted:
        if char in klucz.values():
            for key, value in klucz.items():
                if value == char:
                    decrypted += key
        else:
            decrypted += char
    return decrypted

# Funkcje
print(text)
print(cypher(text))
print(decypher(cypher(text)))

print("\n")

# Onelinery 
print(text)
print(*([klucz.get(character,character) for character in text]),sep="")

print("\n")

print(cypher(text))
print(*[list(klucz.keys())[list(klucz.values()).index(character)] if character in klucz.values() else character for character in cypher(text)],sep="")


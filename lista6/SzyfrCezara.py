def encrypt(string, key):
    result = ""
    for char in string:
        if ord(char) < 91 and ord(char) > 64:
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif ord(char) < 123 and ord(char) > 96:
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(string, key):
    result = ""
    for char in string:
        if ord(char) < 91 and ord(char) > 64:
            result += chr((ord(char) - key - 65) % 65 + 65)
        elif ord(char) < 123 and ord(char) > 96:
            result += chr((ord(char) - key - 97) % 97 + 97)
        else:
            result += char
    return result
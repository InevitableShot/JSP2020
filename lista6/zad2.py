from SzyfrCezara import *

string = input("Podaj tekst do zaszyfrowania: ")
key = int(input("Podaj klucz: "))
print(f'Zaszyfrowany tekst to : {encrypt(string,key)}')
print(f'Odszyfrowany tekst to : {decrypt(encrypt(string,key),key)}')
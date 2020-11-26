digits = {
    "zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8,
    "dziewięć": 9, "dziesięć": 10, "dwadzieścia": 20, "trzydzieści": 30, "czterdzieści": 40, "pięćdziesiąt": 50,
    "jedenaście": 11, "dwanaście": 12, "trzynaście": 13, "czternaście": 14, "piętnaście": 15, "szesnaście": 16,
    "siedemnaście": 17, "osiemnaście": 18, "dziewiętnaście": 19
}

digit = {
    "zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8,
    "dziewięć": 9
}


def word_to_number(d, j=""):
    l1 = 0
    l2 = 0
    if d in digits:
        l1 = digits.get(d)
    if j in digit:
        l2 = digit.get(j)
    print(l1+l2)


number = input("Podaj liczbe od 0 do 59 (slownie): ")
n1 = number.split()
word_to_number(n1[0], n1[1])
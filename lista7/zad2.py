import time
from random import randint
t1 = [randint(0, 20) for i in range(0, 100)]
t2 = [randint(0, 20) for i in range(0, 200)]
t3 = [randint(0, 20) for i in range(0, 300)]


def insertion_sort(tab):
    for index in range(1, len(tab)):
        currentValue = tab[index]
        currentPosition = index
        while currentPosition > 0 and tab[currentPosition - 1] > currentValue:
            tab[currentPosition] = tab[currentPosition - 1]
            currentPosition -= 1
        tab[currentPosition] = currentValue
    return tab


def check(tab):
    t_start = time.process_time()
    insertion_sort(tab)
    t_stop = time.process_time()
    print(
        f'Czas wykonania sortowania dla tablicy {len(tab)} elementowej wynosi: {t_stop-t_start: .9f}s')


def main():
    check(t1)
    check(t2)
    check(t3)
    # Nie ma szans pokazania czasu wykonywania sie tego sortowania dla tak małych tablic


main()

import time
from random import randint
t1 = [randint(0, 20) for i in range(0, 100)]
t2 = [randint(0, 20) for i in range(0, 200)]
t3 = [randint(0, 20) for i in range(0, 300)]


def bubble_sort(tab):
    n = len(tab)
    while n > 1:
        for i in range(0, n-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
        n -= 1
    return tab


def check(tab):
    t_start = time.process_time()
    bubble_sort(tab)
    t_stop = time.process_time()
    print(
        f'Czas wykonania sortowania dla tablicy {len(tab)} elementowej wynosi: {t_stop-t_start: .9f}s')


def main():
    check(t1)
    check(t2)
    check(t3)
    # Nie ma szans pokazania czasu wykonywania sie tego sortowania dla tak małych tablic

main()

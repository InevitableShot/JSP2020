import time
import matplotlib.pyplot as plt


def fib1(n):  # rekurencyjnie
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):  # iteracyjnie
    a = 0
    b = 1
    for i in range(0, n+1):
        print(f"F({i})   {a}")
        a, b = b, a + b


def main():
    n = int(input("Podaj n'ty wyraz ciągu Fibbonaciego: "))
    timer = []
    t_start = time.process_time()
    for i in range(0, n+1):
        t1_start = time.process_time()
        print(f'F({i})   ' + str(fib1(i)))
        t1_stop = time.process_time()
        timer.append(t1_stop - t1_start)
    t_stop = time.process_time()
    print(f"Funkcja wykonana rekurencyjnie trwa: {t_stop - t_start}s\n")
    t_start = time.process_time()
    fib2(n)
    t_stop = time.process_time()
    print(f"Funkcja wykonana iteracyjnie trwa: {t_stop - t_start}s")
    plt.plot([i for i in range(0, n+1)], timer)
    plt.show()


main()

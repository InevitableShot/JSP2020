import time


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
    #t1_start = time.process_time()
    # print(fib1(n))
    #t1_stop = time.process_time()
    t2_start = time.process_time()
    fib2(n)
    t2_stop = time.process_time()
    #print(f"Funkcja wykonana rekurencyjnie trwa: {t1_stop - t1_start}")
    print(f"Funkcja wykonana iteracyjnie trwa: {t2_stop - t2_start}s")


main()

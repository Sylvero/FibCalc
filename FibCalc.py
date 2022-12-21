def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("1) FibCalc")
    print("2) Sylwester skrzypiec")
    print("3) 2.4")
    while (True):
        n = int(input("Podaj numer elementu ciągu Fibonacciego: "))
        result = fibonacci(n)
        print(result)

main()

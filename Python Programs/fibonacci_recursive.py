def fibonacci(n):
    return 1 if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i))

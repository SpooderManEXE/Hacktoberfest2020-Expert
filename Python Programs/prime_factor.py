def prime_factors(num):
    factor = []
    for i in range(2, int(num ** 0.5 + 1)):
        while not num % i:
            factor.append(i)
            num /= i
    if num != 1:
        factor.append(num)
    return factor


if __name__ == '__main__':
    print(prime_factors(120))

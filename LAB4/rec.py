def numbers(n: int) -> None:
    if n < 0:
        return
    print(f'{n} ', end='')
    numbers(n - 1)


def power(x: int, pwr: int) -> int:
    if pwr <= 0:
        return 1
    result: int = x
    result *= power(x, pwr - 1)
    return result


def factorial(n: int) -> int:
    if n <= 0:
        return 1
    result: int = n
    result *= factorial(n - 1)
    # print(f'n={n}, result={result}')
    return result


def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 1
    result = fib(n - 2) + fib(n - 1)
    return result

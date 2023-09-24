from functools import wraps, lru_cache
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__}: {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def sum_list_of_ints(numbers: list) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_list_of_ints(numbers[1:])


def convert_int_to_base(number: int, base: int) -> str:
    if number < base:
        return str(number)
    return convert_int_to_base(number // base, base) + convert_int_to_base(
        number % base, base
    )


@timeit
def sum_list_of_ints2(numbers: list) -> int:
    if not numbers:
        return 0
    if type(numbers[0]) is list:
        return sum_list_of_ints2(numbers[0]) + sum_list_of_ints2(numbers[1:])
    else:
        return numbers[0] + sum_list_of_ints2(numbers[1:])


def factorial(number: int) -> int:
    if number <= 1:
        return number
    return number * factorial(number - 1)


@lru_cache
def fib(number: int) -> int:  # sequence starting at 0 ie 0, 1, 1, 2, 3, 5, 8
    if number <= 1:  # if starting at 1, this would be ... if number in [1, 2]: return 1
        return number
    return fib(number - 1) + fib(number - 2)


def sum_digits(number: int) -> int:
    if number == 0:
        return 0
    return sum_digits(number // 10) + number % 10


def sum_pos_ints(number: int) -> int:
    if number <= 0:
        return number
    return number + sum_pos_ints(number - 2)


def harmonic_sum(n: float) -> float:
    if n <= 2:
        return n
    return 1 / n + harmonic_sum(n - 1)


def power(n: int, pow: int) -> int:
    if pow == 0:
        return 1
    return n * power(n, pow - 1)


def gcd(n1: int, n2: int) -> int:
    low = min(n1, n2)
    high = max(n1, n2)
    if low == 0:
        return high
    elif low == 1:
        return 1
    return gcd(low, high % low)


@timeit
def main():
    # print(sum_list_of_ints([1, 2, 3, 4]))
    # print(convert_int_to_base(number=123, base=10))
    # print(sum_list_of_ints2([1, 2, [3, 4], [5, 6]]))
    # print(factorial(5))
    # print(fib(6))
    # print(sum_digits(345))
    # print(sum_pos_ints(10))
    # print(harmonic_sum(3))
    # print(power(3, 4))
    print(gcd(12, 18))


if __name__ == "__main__":
    main()

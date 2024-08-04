from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    A currying function that returns a function that calculates the Fibonacci number for 
    the given index. This function uses a cache to store the calculated values.

    Returns:
        Callable[[int], int]: A function that calculates the Fibonacci number for the given index.
    """
    cache = {}

    def calculate_fib(number: int) -> int:
        """
        Calculates the Fibonacci number for the given index. 
        Or returns the value from the cache if it exists.

        Args:
            number (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The calculated Fibonacci number.
        """
        if number <= 0:
            return 0
        elif number == 1:
            return 1

        if number in cache:
            return cache[number]

        cache[number] = calculate_fib(number - 1) + calculate_fib(number - 2)
        return cache[number]

    return calculate_fib


def main():
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610


if __name__ == "__main__":
    main()

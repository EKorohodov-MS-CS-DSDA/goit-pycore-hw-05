from typing import Callable
import re

def sum_profit(text: str, func: Callable):
    """
    Calculates the total profit from the text.

    Parameters:
        text (str): The text to calculate the total profit from.
        func (Callable): The function to extract the numbers from the text.    
    """
    total = 0
    for figure in func(text):
        total += figure

    return total

def generator_numbers(text: str):
    """
    A function to process text for extracting numbers.

    Parameters:
        text (str): The text to extract numbers from.

    Yields:
        float: A number extracted from the text.
    """
    numbers = re.findall(r"(\d+\.\d+)", text)
    for number in numbers:
        yield float(number)


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як \
        основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()

"""
## Task
Write a program that prints one line for each number from 1 to 100

* For multiples of three print Fizz instead of the number
* For the multiples of five print Buzz instead of the number
* For numbers which are multiples of both three and five print FizzBuzz

## Instructions
1. Write a test for the smallest piece of functionality.
2. Write the minimum code necessary to pass the test.
3. Refactor the code to improve its quality.
4. Repeat!

"""


def create_return_text_if_dividable_function(divisor: int, replacement: str):
    def return_text_if_dividable(i: int) -> str:
        return f"{'' if i % divisor else replacement}"

    return return_text_if_dividable


RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS = [
    create_return_text_if_dividable_function(3, "Fizz"),
    create_return_text_if_dividable_function(5, "Buzz"),
]


def fizzbuzz(
    i: int, replacement_functions=RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS
) -> str | int:
    return "".join(func(i) for func in replacement_functions) or i

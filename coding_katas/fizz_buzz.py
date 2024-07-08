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


def fizzbuzz(i: int) -> str | int:
    return f"{'' if i % 3 else 'Fizz'}{'' if i % 5 else 'Buzz'}" or i

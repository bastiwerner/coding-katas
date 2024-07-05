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


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

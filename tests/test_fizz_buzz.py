from coding_katas.fizz_buzz import fizzbuzz


def test_fizzbuzz_returns_fizz_for_multiples_of_three():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 != 0:
            assert fizzbuzz(i) == "Fizz"


def test_fizzbuzz_returns_buzz_for_multiples_of_five():
    for i in range(1, 100):
        if i % 5 == 0 and i % 3 != 0:
            assert fizzbuzz(i) == "Buzz"


def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_three_and_five():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            assert fizzbuzz(i) == "FizzBuzz"

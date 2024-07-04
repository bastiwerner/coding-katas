from coding_katas.fizz_buzz import fizzbuzz


def test_fizzbuzz_returns_fizz_for_multiples_of_three():
    assert fizzbuzz(33) == "Fizz"


def test_fizzbuzz_returns_buzz_for_multiples_of_five():
    assert fizzbuzz(50) == "Buzz"


def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_three_and_five():
    assert fizzbuzz(15153015) == "FizzBuzz"

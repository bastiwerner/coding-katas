from coding_katas.fizz_buzz import (
    fizzbuzz,
    RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS,
    create_return_text_if_dividable_function,
)


def test_fizzbuzz_returns_fizz_for_multiples_of_three():
    assert fizzbuzz(33) == "Fizz"


def test_fizzbuzz_returns_buzz_for_multiples_of_five():
    assert fizzbuzz(50) == "Buzz"


def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_three_and_five():
    assert fizzbuzz(15153015) == "FizzBuzz"


def test_fizzbuzz_returns_number_for_non_multiples():
    assert fizzbuzz(91) == 91


def test_fizzbuzz_is_open_for_extension():
    NEW_RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS = RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS

    NEW_RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS.append(
        create_return_text_if_dividable_function(8, "Boink")
    )
    assert (
        fizzbuzz(3 * 5 * 8, NEW_RETURN_TEXT_IF_DIVIDABLE_FUNCTIONS) == "FizzBuzzBoink"
    )

"""
## Description:
Refactor the given code that calculates the total cost of a pizza order.
The function is calculates the total cost of a pizza order based on the following rules:

* Pizza sizes and prices: Small (S): $10, Medium (M): $12, Large (L): $15
* Extra toppings and their prices: Cheese (C): $1, Mushrooms (M): $1.5, Pepperoni (P): $2
* If the order contains more than 3 pizzas, apply a 10% discount to the total.

## Task
* Improve naming conventions for variables and functions.
* Break down the large function into smaller, focused functions.
* Remove code duplication.
* Simplify complex conditional logic.
* Use constants for fixed values like prices.
* Implement a more flexible structure that allows easy addition of new pizza sizes or toppings.

## Instructions
1. Write a test for the smallest piece of functionality.
2. Write the minimum code necessary to pass the test.
3. Refactor the code to improve its quality.
4. Repeat!

"""


class PIZZA_SIZES:
    SMALL = 10.0
    MEDIUM = 12.0
    LARGE = 15.0


class EXTRA_TOPPINGS:
    CHEESE = 1
    MUSHROOM = 1.5
    PEPPERONI = 2


class Pizza:
    def __init__(self, size: PIZZA_SIZES, extra_toppings: list[EXTRA_TOPPINGS] = []):
        self.size = size
        self.extra_toppings = extra_toppings

    def calculate_price(self):
        return self.size + sum(extra_topping for extra_topping in self.extra_toppings)


class PizzaOrder:
    def __init__(self, pizzas: list[Pizza]):
        self.pizzas = pizzas

    def calculate_total_price(self):
        discount_factor = 0.9 if len(self.pizzas) > 3 else 1.0
        return sum(pizza.calculate_price() for pizza in self.pizzas) * discount_factor

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

def p(o):
    t = 0
    for i in o:
        if i['t'] == 'S':
            t += 10
        elif i['t'] == 'M':
            t += 12
        elif i['t'] == 'L':
            t += 15
        if 'e' in i:
            for e in i['e']:
                if e == 'C':
                    t += 1
                if e == 'M':
                    t += 1.5
                if e == 'P':
                    t += 2
    if len(o) > 3:
        t = t * 0.9
    return t

from coding_katas.pizza import Pizza, PIZZA_SIZES, EXTRA_TOPPINGS, PizzaOrder


def test_calculate_pizza_price_with_multiple_orders_returns_correct_total_price():
    order = PizzaOrder(
        pizzas=[
            Pizza(PIZZA_SIZES.SMALL, [EXTRA_TOPPINGS.CHEESE, EXTRA_TOPPINGS.MUSHROOM]),
            Pizza(
                PIZZA_SIZES.LARGE,
                [
                    EXTRA_TOPPINGS.PEPPERONI,
                    EXTRA_TOPPINGS.PEPPERONI,
                    EXTRA_TOPPINGS.CHEESE,
                ],
            ),
            Pizza(PIZZA_SIZES.MEDIUM),
        ]
    )

    assert order.calculate_total_price() == 44.5


def test_discount_applied_on_big_order():
    order = PizzaOrder(
        pizzas=[
            Pizza(PIZZA_SIZES.LARGE),
            Pizza(PIZZA_SIZES.LARGE),
            Pizza(PIZZA_SIZES.LARGE),
            Pizza(PIZZA_SIZES.LARGE),
        ]
    )

    assert order.calculate_total_price() == 4 * PIZZA_SIZES.LARGE * 0.9


def test_adding_more_sizes_and_toppings_is_easy():
    NEW_PIZZA_SIZES = PIZZA_SIZES
    NEW_PIZZA_SIZES.XXL = 20

    NEW_EXTRA_TOPPINGS = EXTRA_TOPPINGS
    NEW_EXTRA_TOPPINGS.GARLIC = 0.5

    order = PizzaOrder(pizzas=[Pizza(NEW_PIZZA_SIZES.XXL, [NEW_EXTRA_TOPPINGS.GARLIC])])

    assert order.calculate_total_price() == 20.5

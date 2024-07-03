from coding_katas.pizza import p

def test_calculate_pizza_price_with_multiple_orders_returns_correct_total_price():
    order = [
        {'t': 'S', 'e': ['C', 'M']},
        {'t': 'L', 'e': ['P', 'P', 'C']},
        {'t': 'M'}
    ]

    t = p(order)

    assert t == 44.5

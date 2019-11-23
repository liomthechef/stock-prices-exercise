import stocks


def test_calculateprofit():
    price_array = [2, 3, 5, 10, 22, 4, 2, 7]
    assert stocks.calculateprofit(price_array) == (20, 2, 22)

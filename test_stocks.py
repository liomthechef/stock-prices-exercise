import stocks


def test_calculatoeprofit():
    price_array = [2, 3, 5, 10, 22, 4, 2, 7]
    assert stocks.calculateprofit(price_array) == 20

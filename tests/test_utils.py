from app.utils import get_price

def test_can_get_price():
    expected = 150
    mod_fct = 1.5
    base_rate = 100

    actual = get_price(base_rate, mod_fct)
    assert actual==expected, f"Expected {expected}, got {actual}"
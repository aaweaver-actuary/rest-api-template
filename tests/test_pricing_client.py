import pytest
from model import calculate_price


class DummyResponse:
    """DummyResponse simulates a requests.Response object for testing."""

    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        return self._json_data


@pytest.fixture
def dummy_post(url, json):
    """Dummy version of requests.post that calculates the price."""
    price = json["base_rate"] * json["modifier"]
    return DummyResponse(200, {"price": price})


def test_calculate_price(monkeypatch):
    """Test the calculate_price function using a dummy requests.post."""

    def dummy_post(endpoint, json):
        # Simulate a successful API response
        return DummyResponse(200, {"price": json["base_rate"] * json["modifier"]})

    monkeypatch.setattr("app.utils.requests.post", dummy_post)
    inputs = {"base_rate": 100.0, "modifier": 1.5}
    expected_price = 100.0 * 1.5
    actual_price = calculate_price(inputs)
    assert actual_price == expected_price, (
        f"Expected {expected_price}, got {actual_price}"
    )

def test_get_price_custom(monkeypatch):
    """Test calculate_price with custom input values using a dummy post."""

    def dummy_post_custom(endpoint, json):
        price = json["base_rate"] * json["modifier"] + 10
        return DummyResponse(200, {"price": price})

    monkeypatch.setattr("app.utils.requests.post", dummy_post_custom)

    inputs = {"base_rate": 100.0, "modifier": 2.0}
    expected_price = 100.0 * 2.0 + 10  # 210.0
    actual_price = calculate_price(inputs)
    assert actual_price == expected_price, (
        f"Expected {expected_price}, got {actual_price}"
    )

def test_get_price_missing_price(monkeypatch):
    """Test calculate_price when API response is missing the 'price' key."""

    def dummy_post_missing(endpoint, json):
        # Returning a 200 response but without the 'price' key
        return DummyResponse(200, {"not_price": 123})

    monkeypatch.setattr("app.utils.requests.post", dummy_post_missing)

    inputs = {"base_rate": 50.0, "modifier": 2.0}
    with pytest.raises(KeyError):
        calculate_price(inputs)

def test_get_price_invalid_input(monkeypatch):
    """Test calculate_price with invalid input that leads to an API error."""
    def dummy_post_invalid(endpoint, json):
        # Simulating an API error response
        return DummyResponse(400, {"error": "Invalid input"})

    monkeypatch.setattr("app.utils.requests.post", dummy_post_invalid)

    # For example, using a non-numeric base_rate
    inputs = {"base_rate": "abc", "modifier": 1.5}
    with pytest.raises(ValueError):
        calculate_price(inputs)

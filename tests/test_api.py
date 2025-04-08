import json
from api.main import PricingInput, app
from fastapi.testclient import TestClient
import pytest
# from model.pricing_model import calculate_price


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def sample_json():
    jdict = {"base_rate": 100.0, "modifier": 1.5}
    return json.dumps(jdict)


@pytest.fixture
def sample_pricing_input():
    return PricingInput(base_rate=100.0, modifier=1.5)


def test_calculate(client, sample_json):
    response = client.post("/calculate", data=sample_json)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json() == {"price": 150.0}, (
        f"Expected price 150.0, got {response.json().get('price')}"
    )


def test_calculate_invalid_input(client):
    invalid_json = json.dumps({"base_rate": "invalid", "modifier": 1.5})
    response = client.post("/calculate", data=invalid_json)
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    # assert '`base_rate` is not a valid float: got "invalid"' in response.text.lower()

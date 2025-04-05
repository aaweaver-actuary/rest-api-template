from model.pricing_model import calculate_price
from api.main import PricingInput


def test_calculate_price_with_very_simple_model():
    inputs = PricingInput(base_rate=100.0, modifier=1.2).model_dump()
    assert calculate_price(inputs) == 120.0, f"Expected 100 * 1.2 = 120.0, got {calculate_price(inputs)}"
    
    inputs = PricingInput(base_rate=80.0, modifier=0.75).model_dump()
    assert calculate_price(inputs) == 60.0, f"Expected 80 * 0.75 = 60.0, got {calculate_price(inputs)}"
    
    inputs = PricingInput(base_rate=50.0, modifier=1.2).model_dump()
    assert calculate_price(inputs) == 60.0, f"Expected 50 * 1.2 = 60.0, got {calculate_price(inputs)}"
    
    inputs = PricingInput(base_rate=0.0, modifier=1.5).model_dump()
    assert calculate_price(inputs) == 0.0, f"Expected 0 * 1.5 = 0.0, got {calculate_price(inputs)}"

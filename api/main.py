from fastapi import FastAPI
from pydantic import BaseModel
from model.pricing_model import calculate_price

app = FastAPI()


class PricingInput(BaseModel):
    base_rate: float
    modifier: float


@app.post("/calculate")
def calculate(input_data: PricingInput):
    price = calculate_price(input_data.model_dump())
    return {"price": price}

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

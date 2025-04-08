from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.pricing_model import calculate_price
from api.logger import api_logger

app = FastAPI()


class PricingInput(BaseModel):
    base_rate: float
    modifier: float


@app.middleware("http")
async def log_requests(request: Request, call_next):
    api_logger.info(f"Incomming Request: {request.method} {request.url}")
    response = await call_next(request)
    api_logger.info(f"Response status: {response.status_code}")
    return response

@app.get("/")
def read_root():
    api_logger.info("Root endpoint called")
    return {"Available endpoints": ["/calculate", "/healthcheck"]}

@app.post("/calculate")
def calculate(input_data: PricingInput):
    api_logger.info(f"Received input data: {input_data}")
    price = calculate_price(input_data.model_dump())
    api_logger.info(f"Calculated price: {price}")
    return {"price": price}


@app.get("/healthcheck")
def healthcheck():
    api_logger.info("Healthcheck endpoint called")
    return {"status": "ok"}

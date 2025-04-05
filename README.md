# rest-api-template

A minimal REST API built with FastAPI that wraps a core insurance pricing model. Designed for internal insurance tooling use cases.

## Features
- REST endpoint to calculate prices using a basic algorithm
- Pydantic validation and type hints
- Modular architecture (business logic separate from API)
- Dockerized for consistent deployment
- Tested with `pytest`

## Quick Start

```bash
# Build and run locally
$ docker build -t internal-pricing-api .
$ docker run -p 8000:8000 internal-pricing-api

# Or run directly
$ uvicorn api.main:app --reload
```

## Endpoint
`POST /calculate`

**Body**:
```json
{
  "base_rate": 100.0,
  "modifier": 1.25
}
```

**Response**:
```json
{
  "price": 125.0
}
```

## Testing
```bash
pytest
```

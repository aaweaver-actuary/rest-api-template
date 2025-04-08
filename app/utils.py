import requests
# import httpx

ENDPOINT="http://localhost:5000/calculate"

def get_price(base=100.0, mod=1, endpoint=ENDPOINT):
    data={"base_rate": base, "modifier": mod}
    
    res = requests.post(ENDPOINT, data=data)

    if res.status_code == 200:
        return res.json()['price']
    else:
        raise ValueError(f"API call failed with status code {res.status_code}")

# async def a_get_price(base=100, mod=1, endpoint=ENDPOINT):
#     data={"base_rate": base, "modifier": mod}
    
#     async with httpx.AsyncClient() as client:
#         res = await client.post(endpoint, json=data)

#         if res.status_code == 200:
#             return res.json()['price']
#         else:
#             raise ValueError(f"API call failed with status code {res.status_code}")

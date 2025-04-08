import requests

ENDPOINT = "http://api:5000/calculate"


def get_price(base: float = 100.0, mod: float = 1, endpoint: str = ENDPOINT):
    """Get the calculated price from the API.

    Parameters
    ----------
    base : float, optional
        The base rate value. Default is 100.0.
    mod : float, optional
        The modifier value. Default is 1.
    endpoint : str, optional
        The URL endpoint for the API. Default is "http://api:5000/calculate".

    Returns
    -------
    float
        The calculated price returned from the API.

    Raises
    ------
    ValueError
        If the API call fails (i.e., response status code is not 200).
    """
    data = {"base_rate": base, "modifier": mod}

    res = requests.post(endpoint, json=data)

    if res.status_code == 200:
        return res.json()["price"]
    else:
        raise ValueError(f"API call failed with status code {res.status_code}")

def calculate_price(inputs: dict) -> float:
    """Calculate a price based on pricing inputs provided by the API call.

    Parameters
    ----------
    inputs : dict
        A dictionary containing keys for the necessary pricing inputs.

    Returns
    -------
    float
        The calculated price.
    """
    base = inputs["base_rate"]
    modifier = inputs["modifier"]
    return base * modifier

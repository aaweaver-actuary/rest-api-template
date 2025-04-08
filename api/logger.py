import logging 

api_logger = logging.getLogger("pricing-api")
api_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
api_logger.addHandler(handler)

# set up file handler
file_handler = logging.FileHandler("api.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
api_logger.addHandler(file_handler)

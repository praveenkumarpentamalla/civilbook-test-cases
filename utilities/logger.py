import logging
import os

def get_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("SeleniumLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logs/test.log", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger

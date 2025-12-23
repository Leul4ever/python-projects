import logging
from unittest import result
## logging configuration
logging.basicConfig ( 
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]

)
logger = logging.getLogger("ArithmeticLogger")

def add(a, b):
    logger.debug(f"Adding {a} and {b} result {a + b}")
    return result

def subtract(a, b):
    logger.debug(f"Subtracting {a} and {b} result {a - b}")
    return result
  

def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b} result {a * b}")
    return result
def divide(a, b):
    if b == 0:
        logger.error("Division by zero attempted")
        return None
    logger.debug(f"Dividing {a} and {b} result {a / b}")
    return result
# Example usage
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)

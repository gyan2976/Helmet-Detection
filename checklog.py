from helmet.logger import logging
from helmet.exception import HelmetException
import sys

logging.info("Hi Gyan")

try:
    a = 7 + 'Gyan'
    print(a)
except Exception as e:
    raise HelmetException(e, sys) from e
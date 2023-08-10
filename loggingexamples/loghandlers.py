# creating log handlers
import logging

logger = logging.getLogger('sample-logger')

logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler('message2.log',mode='w')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s %(asctime)s %(message)s")

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("this is a debug log")
logger.info("this is a info log")
logger.warning("this is a warning log")
logger.critical("this is a critical log")

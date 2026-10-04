import logging

# Logger create
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Common format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)

# File Handler
file_handler = logging.FileHandler("automation.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def test_login():
    logger.debug("Debug message")
    logger.info("Browser Opened")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    assert True

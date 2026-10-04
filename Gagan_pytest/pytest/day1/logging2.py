import logging

logger = logging.getLogger(__name__)


def test_logging():
    logging.info("this is info message")
    logging.warning("this is warning message")
    logging.error("this is error message")
    logging.critical("this is critical message")
    assert True == True

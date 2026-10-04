import logging

logger = logging.getLogger(__name__)


def test_demo():
    logger.warning("Browser opened")
    logger.error("Login failed")
    assert True

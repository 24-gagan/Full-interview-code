import logging

logging.basicConfig(
    filename="test.log",  # Log file name
    level=logging.INFO,  # Logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)


def test_logging():
    logging.info("Test Started")
    logging.warning("This is a warning")
    logging.error("This is an error")
    assert True

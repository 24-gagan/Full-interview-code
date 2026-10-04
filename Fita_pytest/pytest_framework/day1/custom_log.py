import logging
from logging import StreamHandler

# debug-1
# info-2
# warning-3(default priority)
# error-4
# critical-5
# file
logging.basicConfig(
    filename="./test1.txt",
    filemode="w",
    format="%(asctime)s-%(levelname)s-%(message)s,level=logging.DEBUG",
)
# handler-it is used to run both in the stream and in the file
# logging.basicConfig(handlers=StreamHandler(),logging.FileHandler(filename="./test2.txt",mode="w"))
# print(logging.getLogger())
# modify_log = logging.getLogger()
# modify_log.setLevel(logging.CRITICAL)
print(logging.getLogger())
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")

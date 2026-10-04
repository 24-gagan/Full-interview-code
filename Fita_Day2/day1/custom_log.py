import logging

# debug-1
# info-2
# warning-3-- default
# error-4
# critical-5
# print(logging.getLogger())
# modify_log = logging.getLogger()
# modify_log.setLevel(logging.CRITICAL)
#
# print(logging.getLogger())


### file--->
# logging.basicConfig(filename="./test1.txt",
#                     filemode="w",
#                     format="%(asctime)s<-->%(levelname)s %(message)s",
#                     level=logging.DEBUG)

### console--->Stream
# logging.basicConfig(format="%(asctime)s<-->%(levelname)s %(message)s",
#                     level=logging.DEBUG)

### handler
logging.basicConfig(handlers=[logging.StreamHandler(),
                              logging.FileHandler(filename="./test2.txt", mode="w")],
    format="%(asctime)s<-->%(levelname)s %(message)s",
                    level=logging.DEBUG)

logging.debug("this is debug msg")
logging.info("this is info msg")
logging.warning("this is warning msg")
logging.error("this is error msg")
logging.critical("this is critical msg")
import logging

# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w")
formate = "We have next logging message:%(asctime)s:%(levelname)s - %(message)s"

try:
    print(10/0)
except Exception:
    logging.exception("Exception")


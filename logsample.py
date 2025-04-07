import logging
#level is set to warning by default
logging.basicConfig(level=logging.DEBUG)# basic from where message is going to print
logging.debug("hello ,debug!")
logging.info("hello ,info!")
logging.warning("hello ,warning!")
logging.error("hello ,error!")
logging.critical("hello ,critical!")
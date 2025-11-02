import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log", datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)
logging = logging.getLogger()

logging.warning("This code may break in future versions.")
logging.info("This is fine. All is good.")
logging.error("This is an error message, fix it asap!")
logging.critical("Critical issue! Immediate attention required!")

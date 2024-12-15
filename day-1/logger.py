import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.addHandler(logging.StreamHandler())

# clear log file
open('out.log', 'w').close()
# create a file handler
handler = logging.FileHandler('out.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(module)s[#%(lineno)s] - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)
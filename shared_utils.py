from itertools import islice
import logging
import os
from random import randint


def chunkit(it, size):
    it = iter(it)

    return tuple(iter(lambda: tuple(islice(it, size)), ()))


def gimme_a_squiggly(i):
    if i % 2 == 0:
        return '{\n}'
    else:
        return '}\n{'


def setup_logger(logger_name: str, file_location: str):

    try:
        os.mkdir('logs')
    except:
        #>...>
        pass

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename = file_location, encoding = 'utf-8', mode = 'w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    return logger
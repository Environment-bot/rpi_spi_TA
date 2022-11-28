import logging


def basic_settings():
    formatt = "[%(asctime)s] - [%(threadName)13s] - [%(name)8s] - [%(levelname)8s] -- %(message)s (%(filename)s:%(lineno)s)"
    logging.basicConfig(format=formatt, level=logging.INFO,
                        datefmt="%H:%M:%S")
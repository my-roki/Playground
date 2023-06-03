import os
import logging
from datetime import datetime


class LoggerFactory(object):
    _LOGGER = None

    @staticmethod
    def create_logger():
        # root logger
        LoggerFactory._LOGGER = logging.getLogger()
        LoggerFactory._LOGGER.setLevel(logging.INFO)

        # create log directory
        log_dir = "./logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # set formatter
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s:%(filename)s-%(funcName)s:%(lineno)s\n%(message)s")

        # create stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # create file handler
        file_handler = logging.FileHandler(os.path.join(log_dir, datetime.now().strftime("%Y%m%d") + ".log"))
        file_handler.setFormatter(formatter)

        # add handler
        LoggerFactory._LOGGER.addHandler(stream_handler)
        LoggerFactory._LOGGER.addHandler(file_handler)

    @classmethod
    def get_logger(cls):
        return cls._LOGGER


if __name__ == "__main__":
    # test the logger code
    LoggerFactory.create_logger()
    logger = LoggerFactory.get_logger()
    logger.info("test")

import logging
import os

from exec_utils.configloader import Config

cnf = Config()


class Log:
    def __init__(self):
        self.logfile = os.path.join(os.path.normcase(os.path.dirname(__file__)), cnf.get_val("PATHS", "log_file"))

    def logger(self):
        my_logger = logging.getLogger(__name__)
        my_logger.setLevel(logging.DEBUG)
        return my_logger

    @staticmethod
    def log_format():
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def log_file(self):
        logger = self.logger()
        fh = logging.FileHandler(self.logfile)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.log_format())
        if not logger.handlers:
            logger.addHandler(fh)
        return logger

    def connected(self, server, db):
        logger = self.log_file()
        logger.info(f"Connection to {server}, db_name={db} established.")

    def query_start(self, query_name):
        logger = self.log_file()
        logger.info(f"Running {query_name}...")

    def query_finish(self, query_name):
        logger = self.log_file()
        logger.info(f"{query_name} executed with no errors")

    def start_test(self, file_name):
        logger = self.log_file()
        logger.info(f"Starting {file_name}...")

    def finish_test(self, file_name):
        logger = self.log_file()
        logger.info(f"Test {file_name} completed")

    def log_error(self, error_msg):
        logger = self.log_file()
        logger.error(error_msg)

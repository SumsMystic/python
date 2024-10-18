'''
Created on May 15, 2024

@author: Sumeet Agrawal
'''

import pytest
import logging
import inspect


@pytest.mark.usefixtures("suite_setup")
class GreenKartBaseClass:
    

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        self.proj_logger = logging.getLogger(logger_name)
        self.proj_logger.level = logging.INFO
        self.log_file_handler = logging.FileHandler("../logs/default_log_file.log")
        self.log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
        self.log_file_handler.setFormatter(self.log_formatter)
        self.proj_logger.addHandler(self.log_file_handler)
        self.proj_logger.info("\n **************  START NEW RUN  **************")
        return self.proj_logger

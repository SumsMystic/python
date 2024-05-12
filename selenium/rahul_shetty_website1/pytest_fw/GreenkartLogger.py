'''
Created on May 12, 2024

@author: Sumeet Agrawal
'''


import logging
# import pytest

class Greenkart_Logging:
    def __init__(self):
        pass
    
    def get_logger(self, logger_name):
        self.proj_logger = logging.Logger(logger_name)
        self.proj_logger.level = logging.DEBUG
        self.log_file_handler = logging.FileHandler("../logs/default_log_file.log")
        self.log_formatter = logging.Formatter("%(asctime)s : %(name)s : %(message)s")
        self.log_file_handler.setFormatter(self.log_formatter)
        self.proj_logger.addHandler(self.log_file_handler)
        return self.proj_logger

"""
if __name__ == '__main__':
    
    tester = Greenkart_Logging()
    log_obj = tester.get_logger()
    log_obj.info("TESTING IT OUT")
    print("TESTING COMPLETE")    
"""
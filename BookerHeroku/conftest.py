'''
Created on Oct 23, 2024

@author: Sumeet Agrawal
'''

import pytest
import logging
import inspect
from conf_parser import get_config_option


@pytest.fixture(scope="class")
def suite_setup(request):
    """
        BookerHeroku suite setup
    """
    request.cls.proj_logger = logging.getLogger(inspect.stack()[1][3])
    request.cls.proj_logger.info("\n")
    request.cls.proj_logger.info("**************  START NEW RUN  **************")
    request.cls.bs_url = get_config_option('general', 'base_url')    
    request.cls.json_header = {"Content-Type": "application/json"}
    request.cls.auth_token = ""
    request.cls.test_book_booking_id = ""
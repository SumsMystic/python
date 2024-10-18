'''
Created on May 21, 2024

@author: Sumeet Agrawal
'''


from utils.base import GreenKartBaseClass
from pages.GreenKartHomePage import GreenKartHomePg
import pytest


class Test_GreenKart_HomePage(GreenKartBaseClass):
    
    @pytest.mark.negative
    def test_empty_cart(self):
        logger_obj = self.get_logger()
        logger_obj.info("Website loaded")
        
        # Initialize the Page Objects
        HomePgObj = GreenKartHomePg(self.driver_obj, logger_obj)
        
        HomePgObj.click_to_expand_cart()
        logger_obj.info("Clicked on Cart")
        
        assert HomePgObj.is_cart_empty() == True
        logger_obj.info("Empty Cart")
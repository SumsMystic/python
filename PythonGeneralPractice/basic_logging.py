'''
Created on Oct 21, 2024

@author: Sumeet Agrawal
'''


import logging


"""
proj_logger.level = logging.DEBUG
log_file_handler = logging.FileHandler("logs/default_log_file.log")
log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
log_file_handler.setFormatter(log_formatter)
proj_logger.addHandler(log_file_handler)
proj_logger.debug("\n **************  START NEW RUN  **************")
"""

proj_logger = logging.getLogger(__name__)
logging.basicConfig(filename='testing.log', level=logging.INFO)
proj_logger.debug(" **************  START NEW RUN  ************** ")

def test_correct_auth():

    vowel = ['a', 'e', 'i', 'o', 'u']
    word = "devilal"
    count = 0
    for character in word:
        if character in vowel:
            count += 1
    print(count)
    proj_logger.info(" ************** Run Completed ************** ")
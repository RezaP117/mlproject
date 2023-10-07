# for exception handling 
import sys 
#import logging
from src.logger import logging 

def error_message_details(error, error_details:sys):
    # gives us the line number and file for the error 
    _, _, exc_tb = error_details.exc_info()
    # gets file name for where the error is 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno
    error_msg = "Error occured in python script: name [{0}] line number [{1}]\
                error message [{2}]".format(file_name, line_num, str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details = error_detail)

    def __str__(self): 
        return self.error_message

''' 
if __name__ == "__main__":
    try:
        a = 1 / 0 
    except Exception as e: 
        logging.info("DIVIDE BY ZERO ERROR")
        raise CustomException(e, sys)
'''
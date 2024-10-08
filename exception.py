import sys
import logging

def error_message_details(error, error_detail: sys):
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exec_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # Intentional divide by zero error
    except Exception as e:
        logging.info("An error occurred: %s", str(e))
        raise CustomException(e, sys)

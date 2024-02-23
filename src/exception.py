import sys
import logger

"""
why we are importing sys here and passing the argument "error_detail : sys"
os related to files like cd, mkdir
sys related to "interpreter" like import module, exception handling
as we can have many env(interpreter) so which interpreter should i look for this error
obviously the present one in which i have created my env and by forcing sys we are assuring this
so it will access traceback info i.e. which file, line no and kind of error
"""

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        #super().__init__(error_message) #no use of calling parent as again we are updating error_message as self.error_message
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
"""
just to check whether correctly implemented or not
we use name==main thing so below code snippet will work only if run this file directly
if importing this file somewhere else and access it from there, it will not run
as we are using looger.logging.info but we are not getting the msg "logging has started"
which written in the logger.py under the same condition
"""
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logger.logging.info("Divide by zero error")
        raise CustomException(e, sys)

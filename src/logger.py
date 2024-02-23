import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # create log file
logs_path = os.path.join(os.getcwd(), "logs") # adding cd (mlproject) to "logs" folder and this new created log_file
# but we never created "logs" folder by ourself then how could it append this log file in that folder
# below command will make one if its already not present and will not throw an error if already present(exist_ok = true)
os.makedirs(logs_path, exist_ok=True)

"""
don't be confused that why we are joining the paths again
logs_path represents directory only where we are going to store log file
LOG_FILE_PATH represents the full path to a specific log file within the logs_path directory
"""

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

"""
or we can create "logs" folder manually so we don't need logs_path and os.makedirs command
we can simply have to writ these two commands
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(path to logs folder, LOG_FILE)
"""

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

"""
just to check whether implemented or not
"""
if __name__ == "__main__":
    logging.info("Logging has started")
import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) #Meaning that if there is already a file present where we are logging the information , we will continue logging in there and then append to it

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


#To check if logging is working 

# if __name__=="__main__":
#     logging.info("Logging has started")
import logging
import os
from datetime import datetime

# 1️⃣ Create a unique log file name based on current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2️⃣ Create a folder named "logs" in current working directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # fix: 'exits_ok' → 'exist_ok', boolean True capitalized

# 3️⃣ Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # fix typo: 'os.apth' → 'os.path'

# 4️⃣ Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # path to save log
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,      # minimum level to log
)



    
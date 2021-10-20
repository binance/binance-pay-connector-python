import time
import uuid
import hmac
import hashlib

def get_timestamp():
    return int(time.time() * 1000)
  
def random_string():
    random = str(uuid.uuid4())
    random = random.replace("-","") 
    return random[0:32]

def hashing(secrect: str, to_hashing: str):
    return hmac.new(secrect.encode('utf-8'), to_hashing.encode('utf-8'), hashlib.sha512).hexdigest().upper()

def config_logging(logging, logging_devel, log_file=None):
    logging.basicConfig(level=logging_devel, filename=log_file)

import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    APP_VERSION = '1.2.1'
    PUBLIC_IP_URL = os.environ.get('PUBLIC_IP_URL', 'https://ifconfig.me/ip')
    
config = Config()
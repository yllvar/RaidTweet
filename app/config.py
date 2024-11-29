# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    X_API_KEY = os.getenv('X_API_KEY')
    X_API_KEY_SECRET = os.getenv('X_API_KEY_SECRET')
    X_BEARER_TOKEN = os.getenv('X_BEARER_TOKEN')
    X_ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
    X_ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')

config = Config()
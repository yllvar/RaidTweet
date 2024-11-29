import yaml
from dotenv import load_dotenv
import os
from . import logging

logger = logging.setup_custom_logger(__name__)

# Load environment variables once at the start
load_dotenv()

class Config:
    def __init__(self):
        self.load_users()
        self.X_API_KEY = os.getenv('X_API_KEY')
        self.X_API_KEY_SECRET = os.getenv('X_API_KEY_SECRET')
        self.X_BEARER_TOKEN = os.getenv('X_BEARER_TOKEN')
        self.X_ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
        self.X_ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')

    def load_users(self):
        try:
            with open('config.yaml', 'r') as file:
                data = yaml.safe_load(file)
                self.users_to_raid = data.get('users_to_raid', [])
        except FileNotFoundError as e:
            logger.error(f"config.yaml file not found: {e}")
            self.users_to_raid = []
        except yaml.YAMLError as e:
            logger.error(f"Error parsing config.yaml: {e}")
            self.users_to_raid = []

config = Config()

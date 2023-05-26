import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        if os.environ.get("TRELLO_BOARD_ID") == "<TRELLO_BOARD_ID>":
            raise ValueError("Please set .env values")
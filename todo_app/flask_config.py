import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class Config:
    def __init__(self):
        """Base configuration variables."""
        
        if "IS_PROD" in os.environ:
            KVUri = f"https://Luket411TodoAppKeyvault.vault.azure.net"

            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=KVUri, credential=credential) 

            board_id = client.get_secret("trello-board-id")
            trello_token = client.get_secret("trello-token")
            trello_key = client.get_secret("trello-key")
            
        
        
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError(
                "No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        if os.environ.get("TRELLO_BOARD_ID") == "<TRELLO_BOARD_ID>":
            raise ValueError("Please set .env values")

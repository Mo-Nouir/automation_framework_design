import json
import os

BASE_URL = os.getenv("BASE_URL", "https://api.testbank.com")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "your_token_here")

class Config:
    def __init__(self, env="dev"):
        with open("data/config.json") as f:
            configs = json.load(f)
        self.env_config = configs[env]

    @property
    def base_url(self):
        return self.env_config["base_url"]

    @property
    def credentials(self):
        return self.env_config["credentials"]
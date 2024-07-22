import configparser
import os

"""
    CURRENT_VERSION: 1.0
    AUTHOR: Jakub Pankiewicz
    DESCRIPTION: This class create and read configuration file.
        
    **CHANGELOG**
    14.07.2024 |1.0| - Create configuration file implementation.
"""


class AmConfig:
    _instance = None

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.config = configparser.ConfigParser()
            self.config_path = f"{os.environ.get('APPDATA')}\\MyInventory Middleware"
            os.makedirs(self.config_path, exist_ok=True)
            self.initialized = True

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def init_basic_config(self):
        self.config["App Config"] = {
            "Version": "0.0.2",
            "Servers": [
                "Server1",
                "Server2"
            ]
        }
        self.config["Database"] = {
            "Database": "",
            "Password": ""
        }

    def read_config_file(self):
        self.config.read(f"{self.config_path}\\AmConfig.ini")

    def create_config_file(self):
        if not os.path.exists(f"{self.config_path}\\AmConfig.ini"):
            self.init_basic_config()
            with open(f"{self.config_path}\\AmConfig.ini", "w") as configfile:
                self.config.write(configfile)
        else:
            self.read_config_file()

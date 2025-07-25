import json
import os
import datetime

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'testsetting.json'
            )
            with open(config_path, 'r') as file:
                ConfigReader._config = json.load(file)
        return ConfigReader._config

    @staticmethod
    def get_base_url():
        return ConfigReader.load_config().get('base_url')

    @staticmethod
    def get_username():
        return ConfigReader.load_config().get('credentials').get('username')

    @staticmethod
    def get_password():
        return ConfigReader.load_config().get('credentials').get('password')

    @staticmethod
    def get_timeout():
        return float(ConfigReader.load_config().get('timeout').get('implicit', 10))

    @staticmethod
    def get_project_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

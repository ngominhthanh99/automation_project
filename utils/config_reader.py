import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'testsetting.json'
            )
            with open(config_path, 'r') as f:
                ConfigReader._config = json.load(f)
        return ConfigReader._config

    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']

    @staticmethod
    def get_username():
        return ConfigReader.load_config()['credentials']['username']

    @staticmethod
    def get_password():
        return ConfigReader.load_config()['credentials']['password']

    @staticmethod
    def get_timeout():
        return ConfigReader.load_config()['timeout']['implicit']

    @staticmethod
    def get_project_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
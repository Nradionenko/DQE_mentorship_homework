from configparser import ConfigParser, BasicInterpolation
import os


class Config:
    configParser = ConfigParser(interpolation=BasicInterpolation())
    config_folder = os.path.normcase(os.path.dirname(__file__))
    conf_file_path = os.path.join(config_folder, 'configs.ini')

    @classmethod
    def get_val(cls, section, key):
        cls.configParser.read(cls.conf_file_path)
        """Get section details"""
        return cls.configParser.get(section, key)


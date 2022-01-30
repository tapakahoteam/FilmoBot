from configparser import ConfigParser
from .Translations import Translations


app_config = ConfigParser()
app_config.read("Configs/app.ini")

translations = Translations(app_config.get('DEFAULT', 'language'))
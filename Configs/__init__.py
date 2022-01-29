from .languages.english import translations as english
from configparser import ConfigParser
import logging


app_config = ConfigParser()
app_config.read("Configs/app.ini")

lang_config = ConfigParser()
lang_config.read('Configs/languages/english.ini')

class Translations:
    def __init__(self):
        self.language = self.load_language()
        self.all_translations = {
            'english': english
        }
        self.set_locale_translations()
    
    def set_locale_translations(self):
        try: self.locale_translations = self.all_translations[self.language]
        except KeyError:
            logging.error(f'key {self.language} not found in Translations.all_translations')
            raise KeyError
    
    def get(self, key: str, default: any = ''):
        self.update_locale_translations()
        if key in self.locale_translations.keys():
            return self.locale_translations[key]
        return default
    
    def load_language(self) -> str:
        return app_config.get('DEFAULT', 'language')
    
    def update_locale_translations(self):
        language = self.load_language()
        if self.language != language:
            self.language = language
            self.set_locale_translations()

translations = Translations()
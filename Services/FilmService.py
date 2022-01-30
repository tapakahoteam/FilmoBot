from random import randint as rnd

class FilmService:
    @staticmethod
    def get_random_film() -> dict:
        return {
            'name': str(rnd(0,100))
        }
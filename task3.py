import json
import keyword


class DictConverter():
    """класс осуществляет перевод словаря
    в объект класса, создавая из него атрибуты.
    При совпадении атрибута с ключевым словом языка
    к нему добавляется "_"
    """
    def __init__(self, json_dict):
        for key, value in json_dict.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            self.__setattr__(key, self._key_attach(value))

    def _key_attach(self, value: any):
        if isinstance(value, dict):
            return DictConverter(value)
        elif isinstance(value, list):
            return [self._key_attach(v) for v in value]
        else:
            return value


class ColorizeMixin:
    """
    Класс разукрашивающий текст в зеленый
    """
    repr_color_code = 32

    def __str__(self):
        return f'\033[1;{self.repr_color_code};40m{self.__repr__()}\033[0m'


class Advert(ColorizeMixin, DictConverter):
    """
    Класс, преобразующий объявления из словаря в объект,
    позволяющий получать доступ к полям через '.'.
    Поле title  обязательно для всех объявлений
    Поле price должно быть больше 0
    """
    def __init__(self, json_dict: dict):
        if 'title' not in json_dict:
            raise ValueError('No title value in json')

        super().__init__(json_dict)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Price must be >=0')
        else:
            self._price = price


if __name__ == '__main__':
    LESSON_STR = """{
            "title": "python",
            "price": 0,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
            }
            }"""
    lesson = json.loads(LESSON_STR)
    lesson_ad = Advert(lesson)
    print(lesson_ad)

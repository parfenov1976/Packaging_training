"""
Файл класса путей для управления путями к ресурсам приложения
"""

import os
import sys

"""
Импорт модуля os для работы с переменными среды.
Импорт модуля sys для доступа к объектам среды интерпретатора
"""


class Paths:
    """
    Класс путей к ресурсам приложения
    """
    base = os.path.dirname(__file__)  # извлечение абсолютного пути к данному модулю
    # images = os.path.join(base, 'images')
    # icons = os.path.join(images, 'icons')
    # data = os.path.join(base, 'images')
    platform = os.path.join(base, sys.platform)
    """
    Создание пути к папке с ресурсами специфичными для платформы
    Windows - base_dir/win32/...
    MacOS - base_dir/darwin/...
    Linus - base_dir/linus/...
    """
    icons = os.path.join(base, 'icons')  # создание абсолютного пути к папке с иконками

    @classmethod
    def icon(cls, filename: str) -> str:
        """
        Метода класса для возврата пути к файлу при обращении к нему
        :param filename: str - имя файла
        :return: str - строка абсолютного пути к файлу
        """
        return os.path.join(cls.icons, filename)

    # @classmethod
    # def image(cls, filename: str) -> str:
    #     """
    #     Метода класса для возврата пути к файлу при обращении к нему
    #     :param filename: str - имя файла
    #     :return: str - строка абсолютного пути к файлу
    #     """
    #     return os.path.join(cls.images, filename)
    #
    # @classmethod
    # def data(cls, filename: str) -> str:
    #     """
    #     Метода класса для возврата пути к файлу при обращении к нему
    #     :param filename: str - имя файла
    #     :return: str - строка абсолютного пути к файлу
    #     """
    #     return os.path.join(cls.data, filename)

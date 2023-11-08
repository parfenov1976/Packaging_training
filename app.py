"""
Простое приложение для изучения упаковки приложений
"""

import tkinter as tk
import os

"""
Импорт встроенной библиотеки Tkinter для создания графического интерфейса
Импорт модуля os для работы с переменными среды.
"""

# Далее идет код, обеспечивающий показ правильной иконки в панели задач Windows
basedir = os.path.dirname(__file__)  # извлекает путь к данному файлу и записывает его в переменную

try:  # перехват исключения на случай, если данный файл будет запущен не под Windows
    from ctypes import windll  # импорт модуля, дающего доступ к идентификатору процесса Windows

    myappid = 'parfen.hw.simpleapp.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(tk.Tk):
    """
    Класс приложения от супер класса главного окна
    """

    def __init__(self) -> None:
        """
        Конструктор класса приложения
        """
        tk.Tk.__init__(self)  # явный вызов конструктора родительского класса
        self.button_icon = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))  # создание объекта изображения
        # из файла
        self.button = tk.Button(text='My simple app', image=self.button_icon)  # создание экземпляра кнопки с установкой
        # текста на кнопку и иконки
        self.init_ui()  # вызов метода инициализации графического интерфейса

    def init_ui(self) -> None:
        """
        Метод инициализации графического интерфейса приложения
        :return: None
        """
        self.title('Hello World')  # установка имени окна
        self.iconbitmap(os.path.join(basedir, 'icon.ico'))  # установка иконки для заголовка окна
        self.button.pack()  # размещение кнопки в окне приложения с помощью менеджера геометрии
        self.button.bind('<Button-1>', self.handle_button_press)  # назначение сигнала на нажатие кнопки левой кнопкой
        # мыши с привязкой слота ресивера

    def handle_button_press(self, event):
        self.destroy()


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    :return: None
    """
    window = MainWindow()  # создание главного окна приложения
    window.geometry("250x150+300+300")  # задаем размер окна и его расположение
    window.mainloop()  # запуск основного цикла событий


if __name__ == '__main__':
    """
    Условие, необходимое для предотвращения запуска кода верхнего уровня при импортировании данного файла
    """
    main()  # вызов функции запуска кода верхнего уровня приложения

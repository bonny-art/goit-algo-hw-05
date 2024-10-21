"""
Цей модуль містить функцію для читання файлів з автоматичним визначенням
кодування, використовуючи бібліотеку chardet.
"""

import chardet

def read_file(filepath: str) -> str:
    """
    Читає вміст файлу за заданим шляхом з автоматичним визначенням кодування.

    Параметри:
    filepath (str): Шлях до файлу, який потрібно прочитати.

    Повертає:
    str: Вміст файлу, прочитаний як рядок.
    """
    with open(filepath, 'rb') as file:
        raw_data = file.read()  # Читаємо файл у байтовому режимі
        result = chardet.detect(raw_data)  # Визначаємо кодування
        encoding = result['encoding']  # Отримуємо кодування

    with open(filepath, 'r', encoding=encoding) as file:
        return file.read()  # Повертаємо вміст файлу як рядок

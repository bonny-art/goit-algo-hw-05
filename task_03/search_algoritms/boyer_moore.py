"""
Цей модуль реалізує алгоритм Бойера-Мура для пошуку підрядка в рядку.
"""

from typing import List

def boyer_moore(text: str, pattern: str) -> List[int]:
    """
    Реалізує алгоритм Бойера-Мура для пошуку всіх позицій входження 
    підрядка (pattern) в рядок (text).

    Параметри:
    text (str): Текст, в якому буде здійснюватися пошук.
    pattern (str): Підрядок, який потрібно знайти в тексті.

    Повертає:
    List[int]: Список позицій вхождень підрядка в тексті.
    """

    def build_bad_char_table(pattern: str) -> dict:
        """
        Створює таблицю поганих символів для алгоритму Бойера-Мура.

        Параметри:
        pattern (str): Підрядок, для якого будується таблиця.

        Повертає:
        dict: Словник, де ключами є ASCII-коди символів, 
              а значеннями - останні позиції цих символів у підрядку.
        """
        bad_char_table = {}
        for i, char in enumerate(pattern):
            bad_char_table[ord(char)] = i
        return bad_char_table

    m = len(pattern)
    n = len(text)
    bad_char_table = build_bad_char_table(pattern)
    s = 0
    positions = []

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            positions.append(s)
            s += (m - bad_char_table.get(ord(text[s + m]), -1) if s + m < n else 1)
        else:
            s += max(1, j - bad_char_table.get(ord(text[s + j]), -1))

    return positions

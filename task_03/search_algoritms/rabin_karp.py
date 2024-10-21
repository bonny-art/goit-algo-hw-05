"""
Цей модуль реалізує алгоритм Рабіна-Карпа для пошуку підрядка в рядку.
"""

from typing import List

def rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
    """
    Реалізує алгоритм Рабіна-Карпа для пошуку всіх позицій входження 
    підрядка (pattern) в рядок (text).

    Параметри:
    text (str): Текст, в якому буде здійснюватися пошук.
    pattern (str): Підрядок, який потрібно знайти в тексті.
    prime (int): Протонумер, використовуваний для обчислення 
                  хеш-функцій (за замовчуванням 101).

    Повертає:
    List[int]: Список позицій вхождень підрядка в тексті.
    """
    m = len(pattern)
    n = len(text)
    hpattern = 0
    htext = 0
    h = 1
    d = 256
    positions = []

    # Обчислення значення h
    for i in range(m - 1):
        h = (h * d) % prime

    # Обчислення початкових хеш-значень для pattern та text
    for i in range(m):
        hpattern = (d * hpattern + ord(pattern[i])) % prime
        htext = (d * htext + ord(text[i])) % prime

    # Пошук підрядка
    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            # Обчислення нового хеш-значення для text
            htext = (d * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime

    return positions

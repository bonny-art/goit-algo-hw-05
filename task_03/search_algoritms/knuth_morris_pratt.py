"""
Цей модуль реалізує алгоритм Кнута-Морріса-Пратта для пошуку підрядка в рядку.
"""

from typing import List

def knuth_morris_pratt(text: str, pattern: str) -> List[int]:
    """
    Реалізує алгоритм Кнута-Морріса-Пратта для пошуку всіх позицій входження 
    підрядка (pattern) в рядок (text).

    Параметри:
    text (str): Текст, в якому буде здійснюватися пошук.
    pattern (str): Підрядок, який потрібно знайти в тексті.

    Повертає:
    List[int]: Список позицій вхождень підрядка в тексті.
    """

    def compute_lps(pattern: str) -> List[int]:
        """
        Обчислює масив найбільшого префікса, який є одночасно суфіксом 
        (LPS) для заданого підрядка (pattern).

        Параметри:
        pattern (str): Підрядок, для якого буде обчислено масив LPS.

        Повертає:
        List[int]: Масив, де елементи вказують на найбільший префікс 
                   (який є одночасно суфіксом) для підрядка на кожній позиції.
        """
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    positions = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions

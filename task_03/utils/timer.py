"""
Цей модуль містить функцію для проведення тестування алгоритмів пошуку
підрядків, вимірюючи час виконання та повертаючи позиції збігів.
"""

import timeit

def run_test(text: str, pattern: str, algorithm) -> tuple:
    """
    Виконує тестування алгоритму пошуку підрядка на заданому тексті та 
    підрядку, вимірюючи час виконання.

    Параметри:
    text (str): Текст, у якому виконуватиметься пошук.
    pattern (str): Підрядок, який потрібно знайти в тексті.
    algorithm (function): Алгоритм, який буде використовуватися для пошуку.

    Повертає:
    tuple: Кортеж, що містить час виконання у мілісекундах та список позицій 
           збігів.
    """
    # Повертаємо час і позиції збігів
    start_time = timeit.default_timer()  # Початок вимірювання часу
    result = algorithm(text, pattern)  # Виконання алгоритму
    end_time = timeit.default_timer()  # Кінець вимірювання часу
    return (end_time - start_time) * 1000, result  # Переводимо час у мс

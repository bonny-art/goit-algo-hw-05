"""
Цей модуль містить функцію для побудови стовпчикової діаграми,
яка порівнює ефективність різних алгоритмів пошуку підрядка.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_results(results_data, patterns):
    """
    Побудова стовпчикової діаграми для порівняння часів виконання 
    різних алгоритмів пошуку підрядка.

    Параметри:
    results_data (dict): Словник, де ключами є назви алгоритмів, 
                         а значеннями - словники з часами виконання 
                         для кожної статті (article_1, article_2).
    patterns (list): Список підрядків, для яких порівнюються алгоритми.
    """
    pattern_numbers = np.arange(len(patterns))  # Створюємо числовий індекс для підрядків
    bar_width = 0.2  # Ширина стовпчиків

    plt.figure(figsize=(10, 6))  # Створюємо фігуру для стовпчикової діаграми

    # Виводимо стовпчики для кожного алгоритму
    for i, (alg_name, times) in enumerate(results_data.items()):
        # Перший стовпчик для статті 1
        plt.bar(
            pattern_numbers + i * bar_width,
            times['article_1'],
            bar_width,
            label=f'{alg_name} (Стаття 1)'
        )
        # Другий стовпчик для статті 2, знизу
        plt.bar(
            pattern_numbers + i * bar_width,
            times['article_2'],
            bar_width,
            bottom=times['article_1'],
            label=f'{alg_name} (Стаття 2)'
        )

    # Додаємо підписи
    plt.xlabel('Підрядки')
    plt.ylabel('Час (мс)')
    plt.title('Порівняння алгоритмів пошуку підрядка')
    plt.xticks(pattern_numbers + bar_width, [f"Підрядок {i+1}" for i in range(len(patterns))], rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig('results/search_performance.png')  # Збереження графіку у файл
    plt.show()  # Відображення графіку

    # Виведення відповідності номерів підрядків для користувача
    print("Нумерація підрядків:")
    for i, pattern in enumerate(patterns):
        print(f"Підрядок {i+1}: {pattern[:30]}...")  # Виводимо перші 30 символів для зручності

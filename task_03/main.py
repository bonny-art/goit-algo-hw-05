"""
Цей модуль виконує порівняння алгоритмів пошуку підрядків на основі
двох статей. Він використовує три різні алгоритми пошуку підрядків,
вимірює їхню ефективність, генерує звіт у форматі Markdown і
створює графік для візуалізації результатів.
"""

import os

from search_algoritms.knuth_morris_pratt import knuth_morris_pratt
from search_algoritms.boyer_moore import boyer_moore
from search_algoritms.rabin_karp import rabin_karp

from utils.read_file import read_file
from utils.timer import run_test
from utils.report import save_to_md, generate_results_report
from utils.plot import plot_results

if __name__ == "__main__":
    # Читання текстів статей з файлів
    article_1 = read_file("texts/стаття 1.txt")
    article_2 = read_file("texts/стаття 2.txt")

    # Список підрядків для тестування
    patterns = [
        "призводять до вирішення поставленої задачі чи певного завдання",
        "використовується для пошуку елементів у відсортованому масиві",
        "програмісту слід розробити новий алгоритм або поміркувати",
        "розгорнутий список показав найкращі показники швидкодії",
        "найкращі результати по часу формування рекомендацій",
        "саме сховище даних має високі показники ефективності",
        "певного",
        "відсортованому",
        "програмісту",
        "швидкодії",
        "рекомендацій",
        "ефективності"
    ]

    # Словник алгоритмів для тестування
    algorithms = {
        "Knuth-Morris-Pratt": knuth_morris_pratt,
        "Boyer-Moore": boyer_moore,
        "Rabin-Karp": rabin_karp
    }

    # Ініціалізація звіту
    results_report_markdown = "# Порівняння алгоритмів пошуку підрядка\n\n"
    results_report_markdown += (
        "| Алгоритм | Підрядок | Час (Стаття 1) | Позиції (Стаття 1) | "
        "Час (Стаття 2) | Позиції (Стаття 2) |\n"
    )

    results_data = {alg_name: {'patterns': [], 'article_1': [], 'article_2': []} for alg_name in algorithms}

    # Запуск тестування кожного алгоритму для кожного підрядка
    for alg_name, alg in algorithms.items():
        for i, test_pattern in enumerate(patterns):
            time_1, result_1 = run_test(article_1, test_pattern, alg)
            time_2, result_2 = run_test(article_2, test_pattern, alg)

            # Додаємо результати в Markdown звіт
            is_first_row = i == 0  # Перше виклик для цього алгоритму
            results_report_markdown += (
                generate_results_report(
                alg_name,
                test_pattern,
                time_1,
                result_1,
                time_2,
                result_2,
                is_first_row
            )
)

            # Додаємо дані для побудови графіку
            results_data[alg_name]['patterns'].append(test_pattern[:30])
            results_data[alg_name]['article_1'].append(time_1)
            results_data[alg_name]['article_2'].append(time_2)

            # Виведення результатів у консоль
            result_str_1 = f"Позиції: {result_1}" if result_1 else "Підрядок не знайдений"
            result_str_2 = f"Позиції: {result_2}" if result_2 else "Підрядок не знайдений"

            print(f"Алгоритм: {alg_name}, Підрядок: {test_pattern[:30]}...")
            print(f"Стаття 1: Час: {time_1:.3f} ms, {result_str_1}")
            print(f"Стаття 2: Час: {time_2:.3f} ms, {result_str_2}")
            print("-" * 50)

    # Записуємо результати в Markdown файл
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    save_to_md(results_report_markdown, os.path.join(results_dir, 'results.md'))

    # Створюємо стовпчикову діаграму
    plot_results(results_data, patterns)

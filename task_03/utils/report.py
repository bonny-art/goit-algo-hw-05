"""
Цей модуль містить функції для збереження результатів у форматі Markdown
та генерування звіту з результатами алгоритмів пошуку.
"""

def save_to_md(results: str, file_path: str) -> None:
    """
    Зберігає результати вказаного тексту у файл у форматі Markdown.

    Параметри:
    results (str): Результати, які потрібно зберегти у файл.
    file_path (str): Шлях до файлу, в який буде збережено результати.

    Повертає:
    None
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(results)  # Записуємо результати у файл

def generate_results_report(alg_name: str, pattern: str, time_1: float,
                             result_1: list, time_2: float,
                             result_2: list, is_first_row: bool = False) -> str:
    """
    Генерує рядок у форматі Markdown для звіту з результатами виконання алгоритму.

    Параметри:
    alg_name (str): Назва алгоритму.
    pattern (str): Підрядок, для якого виконувалось пошук.
    time_1 (float): Час виконання першого алгоритму.
    result_1 (list): Результати пошуку для першого алгоритму.
    time_2 (float): Час виконання другого алгоритму.
    result_2 (list): Результати пошуку для другого алгоритму.
    is_first_row (bool): Вказує, чи це перший рядок таблиці (задає заголовки).

    Повертає:
    str: Рядок у форматі Markdown з результатами виконання алгоритмів.
    """
    if is_first_row:
        result_md = "|---|---|---|---|---|---|\n"  # Заголовки таблиці
    else:
        result_md = ""

    result_md += (f"| {alg_name} | {pattern[:30]}... | {time_1:.3f} ms | "
                  f"{' '.join(map(str, result_1)) if result_1 else 'Підрядок не знайдений'} | "
                  f"{time_2:.3f} ms | {' '.join(map(str, result_2)) if result_2 else 'Підрядок не знайдений'} |\n")

    return result_md

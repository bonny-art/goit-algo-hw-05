"""
Цей модуль містить функцію для виконання двійкового пошуку у відсортованому масиві дробових чисел.
Результатом пошуку є кортеж, що містить кількість ітерацій та верхню межу (найменше число, яке більше
або дорівнює шуканому). Якщо шукане число більше за всі елементи масиву, повертається повідомлення 
про те, що число більше всіх елементів масиву.

Функція `binary_search` використовується для пошуку заданого значення в відсортованому масиві.
Також включені приклади тестування в блоці `if __name__ == "__main__"`.
"""

from typing import List, Tuple, Optional

def binary_search(arr: List[float], target: float) -> Tuple[int, Optional[float]]:
    """
    Виконує двійковий пошук у відсортованому масиві дробових чисел.

    Args:
        arr (List[float]): Відсортований масив дробових чисел.
        target (float): Значення, яке потрібно знайти.

    Returns:
        Tuple[int, Optional[float]]: Кортеж, що містить:
            - Кількість ітерацій, необхідних для пошуку.
            - Верхню межу (найменше значення в масиві, яке більше або дорівнює target).
              Якщо значення більше за всі елементи масиву, повертається повідомлення.
    """
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value < target:
            left = mid + 1
        else:
            upper_bound = mid_value
            right = mid - 1

    # Якщо upper_bound не знайдено, або воно менше за target
    if upper_bound is None or upper_bound < target:
        upper_bound = arr[left] if left < len(arr) else 'Шукане число більше всіх чисел у масиві'

    return iterations, upper_bound


if __name__ == "__main__":
    sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]

    # Перелік тестових випадків у форматі (шукане значення, опис)
    test_cases = [
        (0.5, "Шукане значення менше за всі елементи масиву"),
        (3.3, "Шукане значення дорівнює одному з елементів масиву"),
        (6.0, "Шукане значення більше за всі елементи масиву"),
        (3.4, "Шукане значення знаходиться між двома елементами масиву")
    ]

    # Виконання кожного тесту
    for target_value, description in test_cases:
        result = binary_search(sorted_array, target_value)
        print(f"\n{description}:")
        print(f"Цільове значення: {target_value}, Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")

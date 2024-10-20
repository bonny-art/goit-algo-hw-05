"""
Модуль для реалізації хеш-таблиці.

Цей модуль містить клас HashTable, який реалізує базові операції хеш-таблиці:
вставку, отримання та видалення пар ключ-значення. 
"""
class HashTable:
    """
    Простий клас для реалізації хеш-таблиці з методами вставки, отримання та видалення пар ключ-значення.

    Attributes:
        size (int): Розмір хеш-таблиці.
        table (list): Список, що містить списки для обробки колізій.
    """

    def __init__(self, size: int):
        """
        Ініціалізує хеш-таблицю з заданим розміром.

        Args:
            size (int): Розмір хеш-таблиці.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key: str) -> int:
        """
        Обчислює хеш для заданого ключа.

        Args:
            key (str): Ключ, для якого потрібно обчислити хеш.

        Returns:
            int: Хеш значення для ключа.
        """
        return hash(key) % self.size

    def insert(self, key: str, value: int) -> bool:
        """
        Вставляє пару ключ-значення в хеш-таблицю.

        Args:
            key (str): Ключ, що вставляється.
            value (int): Значення, що вставляється.

        Returns:
            bool: True, якщо вставка була успішною, False в іншому випадку.
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key: str) -> int:
        """
        Отримує значення за заданим ключем.

        Args:
            key (str): Ключ, для якого потрібно отримати значення.

        Returns:
            int: Значення, що відповідає ключу, або None, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key: str) -> bool:
        """
        Видаляє пару ключ-значення за заданим ключем.

        Args:
            key (str): Ключ, що потрібно видалити.

        Returns:
            bool: True, якщо видалення було успішним, False, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][index]
                    return True
        return False

if __name__ == "__main__":
    # Створюємо хеш-таблицю з розміром 5
    H = HashTable(5)

    # Вставляємо пари ключ-значення
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    # Тестуємо отримання значень
    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    # Тестуємо видалення ключа
    H.delete("orange")      # Видаляємо "orange"
    print(H.get("orange"))  # Виведе: None (оскільки "orange" видалено)

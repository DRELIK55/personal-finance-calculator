"""Модуль калькулятора."""
import os
from operations import add, subtract, multiply, divide


class Calculator:
    """Класс для выполнения математических операций и хранения истории."""

    def __init__(self):
        """Инициализация калькулятора."""
        self.history = []

    def calculate(self, a, b, operation):
        """Выполняет операцию и сохраняет результат в историю."""
        result = None
        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = subtract(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            if b == 0:
                print("Error: Division by zero!")
                return None
            result = divide(a, b)
        else:
            print("Unknown operation")
            return None
        self.history.append(f"{a} {operation} {b} = {result}")
        return result

    def clear_history(self):
        """Очищает историю операций."""
        self.history = []

    def save_history(self, filename):
        """Сохраняет историю в файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            for item in self.history:
                f.write(item + '\n')

    def load_history(self, filename):
        """Загружает историю из файла."""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                self.history = [line.strip() for line in f.readlines()]
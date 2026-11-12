# Импортируем ВСЁ из модулей
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print("=== Запуск через dirty_main.py ===")
    # Функции доступны напрямую, без указания имени модуля
    calculate_salary()
    get_employees()
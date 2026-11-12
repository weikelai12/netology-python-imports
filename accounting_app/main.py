import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    # 3. Вывод текущей даты с помощью модуля datetime
    current_date = datetime.date.today()
    print(f"=== Запуск программы 'Бухгалтерия' ===")
    print(f"Текущая дата: {current_date}")
    print("-" * 40)

    # 2. Вызов импортированных функций
    get_employees()
    calculate_salary()
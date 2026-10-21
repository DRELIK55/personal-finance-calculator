operations = []

def add_operation():
    print("\n--- Добавление операции ---")
    op_type = input("Тип (доход/расход): ").strip().lower()
    if op_type not in ['доход', 'расход']:
        print("Ошибка: введите 'доход' или 'расход'")
        return
    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Ошибка: сумма должна быть числом")
        return
    category = input("Категория: ").strip()
    date = input("Дата (ДД.ММ.ГГГГ): ").strip()
    
    operations.append({
        "type": op_type,
        "amount": amount,
        "category": category,
        "date": date
    })
    print("Операция успешно добавлена!")

def show_operations():
    print("\n--- Список операций ---")
    if not operations:
        print("Операций пока нет.")
        return
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op['date']} | {op['type'].capitalize()} | {op['category']} | {op['amount']} руб.")

def show_balance():
    print("\n--- Текущий баланс ---")
    income = sum(op["amount"] for op in operations if op["type"] == "доход")
    expense = sum(op["amount"] for op in operations if op["type"] == "расход")
    balance = income - expense
    print(f"Доходы: {income} руб.")
    print(f"Расходы: {expense} руб.")
    print(f"Баланс: {balance} руб.")

def main():
    while True:
        print("\n=== Калькулятор финансов ===")
        print("1. Добавить операцию")
        print("2. Показать все операции")
        print("3. Показать баланс")
        print("0. Выход")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            add_operation()
        elif choice == "2":
            show_operations()
        elif choice == "3":
            show_balance()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
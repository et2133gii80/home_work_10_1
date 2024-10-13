import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.sorting_transactions import sorting_transactions_by_description
from src.utils import transaction_data
from src.widget import get_date, mask_account_card
from src.work_with_csv_excel import get_transactions_csv, read_xlsx

"""Путь до Json файла"""
current_json = os.path.dirname(os.path.abspath(__file__))
rel_json_file_path = os.path.join(current_json, "../data/operations.json")
josn_file_path = os.path.abspath(rel_json_file_path)

"""Путь до csv файла"""
current_csv = os.path.dirname(os.path.abspath(__file__))
rel_csv_file_path = os.path.join(current_csv, "../data/transactions.csv")
csv_file_path = os.path.abspath(rel_csv_file_path)

"""Путь до excel файла"""
current_excel = os.path.dirname(os.path.abspath(__file__))
rel_excel_file_path = os.path.join(current_excel, "../data/transactions_excel.xlsx")
excel_file_path = os.path.abspath(rel_excel_file_path)


def main():
    """Программа приветствует пользователя"""
    hello_user = input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    if hello_user == "1":
        print("Программа: Для обработки выбран JSON-файл")
        transaction = transaction_data(josn_file_path)
    elif hello_user == "2":
        print("Программа: Для обработки выбран CSV-файл")
        transaction = get_transactions_csv(csv_file_path)
    elif hello_user == "3":
        print("Программа: Для обработки выбран EXCEL-файл")
        transaction = read_xlsx(excel_file_path)

    """После пользователь выбирает статус интересующих его операций"""
    state_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        ).upper()
        if status not in state_list:
            print(f'Статус операции "{status}" недоступен.')
        else:
            break
    filtered_transactions = filter_by_state(transaction, status)

    sort = input("Отсортировать операции по дате? Да/Нет. ").lower()
    if sort == "да":
        if input("Отсортировать по возрастанию или по убыванию? ").lower() == "по возрастанию":
            date_flag = False
        else:
            date_flag = True
        filtered_transactions = sort_by_date(filtered_transactions, date_flag)
    print_rub = input("Выводить только рублевые тразакции? Да/Нет")
    if print_rub.lower() == "да":
        rub_sort = filter_by_currency(filtered_transactions, "RUB")
        filtered_transactions = list(rub_sort)[::-1]
    filter_by_word = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    if filter_by_word.lower() == "да":
        word = input("Введите слово: ")
        filtered_transactions = sorting_transactions_by_description(filtered_transactions, word)
    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке:{len(filtered_transactions)}")
        for i in filtered_transactions:
            currency = i["operationAmount"]["currency"]["name"]
            i_data = get_date(i["date"])
            if i["description"] == "Открытие вклада":
                from_to = mask_account_card(i["to"])
            else:
                from_to = mask_account_card(i["from"]) + " -> " + mask_account_card(i["to"])

            amount = i["operationAmount"]["amount"]
            print(f"{i_data} {i["description"]}\n{from_to}\n Сумма: {round(float(amount))} {currency}")


if __name__ == "__main__":
    main()

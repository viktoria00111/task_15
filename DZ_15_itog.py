# import decimal
# import logging
# import argparse

# # Настройки логирования
# logging.basicConfig(
#     filename='bank_operations.log',
#     filemode='a',  # 'a' для добавления в конец файла
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding='utf-8'
# )

# MULTIPLICITY = 50
# PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
# MIN_REMOVAL = decimal.Decimal(30)
# MAX_REMOVAL = decimal.Decimal(600)
# PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
# COUNTER4PERCENTAGES = 3
# RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
# RICHNESS_SUM = decimal.Decimal(10_000_000)

# bank_account = decimal.Decimal(0)
# count = 0
# operations = []

# def check_multiplicity(amount):
#     if (amount % MULTIPLICITY) != 0:
#         logging.error(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#         return False
#     return True

# def deposit(amount):
#     global bank_account, count
#     if not check_multiplicity(amount):
#         logging.info(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#         return False
#     count += 1
#     bank_account += amount
#     operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
#     logging.info(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
#     return True

# def withdraw(amount):
#     global bank_account, count
#     percent = amount * PERCENT_REMOVAL
#     percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
#     if bank_account >= amount + percent:
#         count += 1
#         bank_account -= (amount + percent)
#         operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Сумма на карте {int(bank_account)} у.е.')
#         logging.info(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Сейчас на карте осталось {int(bank_account)} у.е.')
#     else:
#         operations.append(f'Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е.')
#         logging.error(f'Недостаточно средств на счете. На карте - {int(bank_account)} у.е., а сумма снятия с комиссией {amount + int(percent)} у.е.')

# def exit():
#     global bank_account, operations
#     if bank_account > RICHNESS_SUM:
#         percent = bank_account * RICHNESS_PERCENT
#         bank_account -= percent
#         operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT*100}% в сумме {percent} у.е. Итого {bank_account} у.е.')
#         logging.info(f'Вычтен налог на богатство {RICHNESS_PERCENT*100}% в сумме {percent} у.е. Итого {bank_account} у.е.')
#     operations.append(f'Возьмите карту на которой {bank_account} у.е.')

# def main(deposit_amount, withdraw_amount):
#     deposit(decimal.Decimal(deposit_amount))
#     withdraw(decimal.Decimal(withdraw_amount))
#     exit()
#     for op in operations:
#         print(op)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Обработка банковских операций.')
#     parser.add_argument('--deposit', type=float, help='Сумма для пополнения', default=0)
#     parser.add_argument('--withdraw', type=float, help='Сумма для снятия', default=0)
#     args = parser.parse_args()
#     main(args.deposit, args.withdraw)

#Возьмите любые 1-3 задания из прошлых домашних заданий. 
#Добавьте к ним логирование ошибок и полезной информации. 
#Также реализуйте возможность запуска из командной строки с передачей параметров. 
#Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание. 
#"Незачет" ставится, если Слушатель не выполнил задание. 
#Критерии оценивания: 1 - Слушатель написал корректный код для задачи, добавил к ним логирование ошибок и полезной информации.

# Функция получает на вход текст ,например: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import logging
import datetime
from time import asctime


dict_weekday = {"понедельник": 1,
                "вторник": 2,
                "среда": 3,
                "четверг": 4,
                "пятница": 5,
                "суббота": 6,
                "воскресенье": 7}

dict_month = {"января": 1,
              "февраяля": 2,
              "марта": 3,
              "апреля": 4,
              "мая": 5,
              "июня": 6,
              "июля": 7,
              "августа": 8,
              "сентября": 9,
              "октября": 10,
              "ноября": 11,
              "декабря": 12}

def func (data_str):
    data_str = data_str.split()
    now_year = datetime.datetime.now().year     # текущий год
    num_weekday = int(data_str[0][0])           # номер недели
    num_day = dict_weekday [data_str[1]]        # день недели
    num_month = dict_month [data_str[2]]        # месяц

    day_one_month = datetime.datetime.strptime(f'{now_year}-{num_month}-01', '%Y-%m-%d').weekday()
    # номер дня недели 1-го числа в месяце (0-понедельник, 6-воскресенье)

    day_relative = (num_weekday-(1 if day_one_month<num_day else 0))*7 + num_day
    # относительный день в месяце (если считать 1 день любого месяца - понедельником)

    day = day_relative - day_one_month
    # фактический день в месяце = относительный день минус номер дня недели 1-го числа в месяце

    result_date = datetime.datetime.strptime(f'{now_year}-{num_month}-{day}', '%Y-%m-%d').strftime("%Y-%m-%d")
    return result_date



my_format = "{asctime:<15} - {levelname:<10} - {msg}"
logging.basicConfig(filename='./log15.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, style='{', format=my_format)
logger = logging.getLogger(__name__)

date_list = ["4-ый четверг октября",
             "1-ый понедельник ноября",
             "5-ая суббота сентября",
             "1-ый вторник мая",
             "5-ая суббота марта",
             "5-ый четверг июня"]
for i_date in date_list:
    try:
        data_res = func(i_date)
        print (f"{i_date}\t{data_res}")
        logger.info (msg=f"{i_date:.<30}{data_res}")
    except ValueError as e:
        print (f"{i_date}\t<- ошибка даты!")
        logger.error (msg=f"{i_date:.<30}!ошибка даты!")
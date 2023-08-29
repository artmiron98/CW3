import json
import datetime as dt

'''Конвертация json в dict'''
def load_operations_from_json(path):
    file = open(path, encoding='utf-8')
    return json.load(file)

'''Подготовка словаря'''
def prepare_operations(row_operations):
    clear_operations = []
    for op in row_operations:
        if 'date' not in op or 'to' not in op or 'from' not in op:
            continue
        op_date = dt.datetime.fromisoformat(op['date'])
        op_amount = op['operationAmount']['amount']
        op_currency = op['operationAmount']['currency']['code']
        op_state =  op['state']
        op_description = op['description']
        op_from = op['from']
        op_to = op['to']
        operation = {'date' : op_date, 'amount' : op_amount, 'currency' : op_currency,'state': op_state, 'description' : op_description, 'from' : op_from, 'to' : op_to}
        clear_operations.append(operation)
    return clear_operations

'''Извлечение даты для сортировки'''
def get_date(dict_item):
    return dict_item['date']

'''Сортировка словаря по дате'''
def sorted_operations(operations):
    executed_op = []
    for i in operations:
        if i['state'] == 'EXECUTED':
            executed_op.append(i)
    return sorted(executed_op, key=get_date, reverse=True)

'''Получение последних n операций'''
def get_last_operations(operations, number):
    last_operations = []
    for i in range(number):
        last_operations.append(operations[i])
    return last_operations

'''Маскировка номера счета/карты'''
def mask_account_number(account_number):
    split_account_number = account_number.split(' ')
    last_value = split_account_number[-1]
    if len(last_value) == 16:
        return f'{" ".join(split_account_number[:-1])} {last_value[:4]} {last_value[4:6]}** **** {last_value[12:]}'
    else:
        return f'{" ".join(split_account_number[:-1])} **{last_value[-4:]}'


'''Перевод даты в нужный формат'''
def correct_date_format(op_date):
    return dt.datetime.strftime(op_date, '%d.%m.%Y')








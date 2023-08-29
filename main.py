from src import funcst as f

'''Форматируем JSON в DICT'''
operations = f.load_operations_from_json('operations.json')
'''Создаем словарь с подготовленными данными'''
operations_prepared = f.prepare_operations(operations)
'''Создаем отсортированный по дате словарь'''
sorted_dict = f.sorted_operations(operations_prepared)
'''Указываем сколько операций выводит программа'''
last_5 = f.get_last_operations(sorted_dict, 5)

print(operations_prepared)

'''Основная программа'''
for operation in last_5:
   print(f"""{f.correct_date_format(operation['date'])} {operation['description']}
{f.mask_account_number(operation['from'])} -> {f.mask_account_number(operation['to'])}
{operation['amount']} {operation['currency']}.\n""")
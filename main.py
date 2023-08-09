import funcs as f

operations = f.read_json()
correct_operations = {}

for operation in operations:
    for i in operation:
        correct_operations['date_new'] = f.convert(operation['date'])
        #correct_operations['description'] = operation['description']
    #print(operation['id'])
    #print(f.convert(operation['date']))
print(correct_operations)
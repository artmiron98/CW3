import json
import datetime as dt
def read_json():
    file = open('operations.json', encoding='utf-8')
    return json.load(file)


def convert(date_time):
    format = '%Y-%m-%d'
    datetime_str = dt.datetime.strptime(date_time[:10], format)
    return datetime_str


from src import funcst as f
import datetime as dt
#import pytest


test_operations = f.load_operations_from_json('operations_test.json')
test_prep_operations = f.prepare_operations(test_operations)
test_get_last_operation = f.get_last_operations(test_prep_operations, 4)
def test_load_operations_from_json():
    assert f.load_operations_from_json('operations_test.json') == test_operations

def test_prepare_operations():
    assert f.prepare_operations(test_operations) == test_prep_operations

def test_get_last_operations():
    assert f.get_last_operations(test_prep_operations, 4) == test_get_last_operation



def test_mask_account_number():
    assert f.mask_account_number('Счет 48894435694657014368') == 'Счет **4368'
    assert f.mask_account_number('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert f.mask_account_number('Maestro 3928549031574026') == 'Maestro 3928 54** **** 4026'



def test_correct_date_format():
    assert f.correct_date_format(dt.datetime(2018, 4, 16, 17, 34, 19, 241289)) == '16.04.2018'
    assert f.correct_date_format(dt.datetime(2018, 3, 2, 2, 3, 11, 563721)) == '02.03.2018'
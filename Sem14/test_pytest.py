from remove_ch import remove_char
import pytest


# добавлять мессадж
def test_no_change():
    assert remove_char('qwer') == 'qwer'


def test_result_is_str():
    assert isinstance(remove_char('qwer'), str)

def test_space():
    assert ' ' in remove_char('qwer qwer')


def test_none():
    assert remove_char('qwer') is not None


if __name__ == '__main__':
    pytest.main(['-vv'])

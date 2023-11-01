from control_num import Rect
import pytest


@pytest.fixture()
def r1():
    return Rect(2, 3)


@pytest.fixture()
def r2():
    return Rect(4, 3)


def test_valueerror():
    with pytest.raises(ValueError):
        Rect(2, -2)


def test_sum_result_is_rect(r1, r2):
    assert isinstance(r1 + r2, Rect)


def test_per(r2):
    assert r2.per() == 14


if __name__ == '__main__':
    pytest.main(['-vv'])

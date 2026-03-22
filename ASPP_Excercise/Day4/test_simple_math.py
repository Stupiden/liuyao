import pytest
import simple_math


def test_add():
    assert simple_math.add(2, 3) == 5
    assert simple_math.add(-1, 1) == 0
    assert simple_math.add(0, 0) == 0


def test_subtract():
    assert simple_math.subtract(5, 3) == 2
    assert simple_math.subtract(3, 5) == -2
    assert simple_math.subtract(0, 0) == 0


def test_multiply():
    assert simple_math.multiply(4, 3) == 12
    assert simple_math.multiply(-2, 3) == -6
    assert simple_math.multiply(0, 100) == 0


def test_divide():
    assert simple_math.divide(10, 2) == 5
    assert simple_math.divide(3, 2) == 1.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        simple_math.divide(1, 0)
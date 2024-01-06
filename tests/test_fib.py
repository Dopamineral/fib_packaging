import pytest

from fib.fib import fib


def test_fib_0():
    assert fib(0) == 0


def test_fib_1():
    assert fib(1) == 1


def test_fib_2():
    assert fib(2) == 1


def test_fib_3():
    assert fib(3) == 2


def test_fib_10():
    assert fib(10) == 55


def test_fib_negative():
    with pytest.raises(RecursionError):
        fib(-1)

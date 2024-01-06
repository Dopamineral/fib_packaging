import pytest
from main import fib

def test_fib_zero():
    assert fib(0) == 0

def test_fib_one():
    assert fib(1) == 1

def test_fib_two():
    assert fib(2) == 1

def test_fib_ten():
    assert fib(10) == 55

def test_fib_negative():
    with pytest.raises(RecursionError):
        fib(-1)
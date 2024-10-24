from maths import (
    add,
    subtract,
    divide,
    multiply
)
def test_add():
    assert add(2,10) == 12
def test_subtract():
    assert subtract(2,10) == -8
def test_divide():
    assert divide(2,10) == 0.2
def test_multiply():
    assert multiply(2,10) == 2
assert("hi" ==  "Fail on purpose")
import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98
    


def test_fun5():
    # Normal division
    assert calculator.fun5(10, 2) == 5
    assert calculator.fun5(9, 3) == 3
    assert calculator.fun5(-10, 2) == -5
    assert calculator.fun5(7, 2) == 3.5
    
    # Test zero division error
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(10, 0)

def test_fun6():
    # Power/exponent tests
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 2) == 25
    assert calculator.fun6(10, 0) == 1
    assert calculator.fun6(2, -1) == 0.5
    assert calculator.fun6(-2, 3) == -8

def test_fun7():
    # Square root tests
    assert calculator.fun7(4) == 2
    assert calculator.fun7(9) == 3
    assert calculator.fun7(16) == 4
    assert calculator.fun7(0) == 0
    assert calculator.fun7(2) == pytest.approx(1.414, rel=1e-2)
    
    # Test negative number error
    with pytest.raises(ValueError):
        calculator.fun7(-4)

def test_fun8():
    # Modulo tests
    assert calculator.fun8(10, 3) == 1
    assert calculator.fun8(20, 6) == 2
    assert calculator.fun8(15, 4) == 3
    assert calculator.fun8(10, 5) == 0
    
    # Test zero divisor error
    with pytest.raises(ZeroDivisionError):
        calculator.fun8(10, 0)

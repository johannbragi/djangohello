import mathlib


def test_calc_addition():
    # Verify the output of `calc_addition` function
    output = mathlib.calc_addition(2, 4)
    assert output == 6


def test_calc_substraction():
    # Verify the output of `calc_substraction` function
    output = mathlib.calc_substraction(2, 4)
    assert output == -2


def test_calc_multiply():
    # Verify the output of `calc_multiply` function”””
    output = mathlib.calc_multiply(2, 4)
    assert output == 8


def test_calc_multiply2():
    # Verify the output of `calc_multiply` function”””
    output = mathlib.calc_multiply(2, 5)
    assert output == 10


def test_calc_multiply_should_fail():
    # Verify the output of `calc_multiply` function”””
    output = mathlib.calc_multiply(2, 5)
    assert output == 8

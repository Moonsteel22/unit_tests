import pytest

from unit_tests.quadratic_equation import solve_quadratic_equation, EPSILON


def test_a_coef() -> None:
    """0*x^2 + 2x + 1 = 0, a=0, b=2, c=1"""
    with pytest.raises(ValueError):
        solve_quadratic_equation(a=EPSILON / 10, b=2, c=1)

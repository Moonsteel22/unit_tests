from typing import Any
from unittest.mock import Mock

from unit_tests.quadratic_equation import solve_quadratic_equation, EPSILON


def test_zero_discriminant() -> None:
    """x^2 + 2x + 1 = 0, a=1, b=2, c=1"""
    discriminant_mock: Any = Mock(return_value=EPSILON / 10)

    roots = solve_quadratic_equation(
        a=1, b=2, c=1, discriminant_formula=discriminant_mock
    )

    assert len(roots) == 1

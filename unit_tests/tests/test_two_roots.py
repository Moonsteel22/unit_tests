from unit_tests.quadratic_equation import solve_quadratic_equation


def test_zero_roots() -> None:
    """x^2 - 1 = 0, a=1, b=0, c=-1"""
    assert len(solve_quadratic_equation(a=1, b=0, c=-1)) == 2

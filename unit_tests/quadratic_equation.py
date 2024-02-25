import math
from typing import Callable

EPSILON: float = 0.0001


def solve_quadratic_equation(
    a: float,
    b: float,
    c: float,
    discriminant_formula: Callable[[float, float, float], float] = lambda a, b, c: b**2
    - 4 * a * c,
) -> tuple:
    if abs(a) < EPSILON:
        raise ValueError("a == 0")
    discriminant: float = discriminant_formula(a, b, c)
    if discriminant > EPSILON:
        x1: float = -b + math.sqrt(discriminant)
        x2: float = -b - math.sqrt(discriminant)
        return x1, x2
    if abs(discriminant) < EPSILON:
        return (-b,)
    return tuple()

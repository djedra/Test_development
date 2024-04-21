def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

def solution(a: float, b: float, c: float) -> tuple:
    if discriminant(a, b, c) < 0:
        return None
    elif discriminant(a, b, c) == 0:
        return -b / (2*a)
    else:
        return ((-b+discriminant(a, b, c)**0.5) / (2*a), (-b-discriminant(a, b, c)**0.5) / (2*a))
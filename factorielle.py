"""
C'est le module "exemple".

Le module d'exemple fournit une fonction, factoriel (). Par example,

>>> factorielle(5)
120
"""

def factorielle(n):
    """Renvoie la factorielle de n,  n etant un entier exact  >= 0.

    >>> [factorielle(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorielle(30)
    265252859812191058636308480000000
    >>> factorielle(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    factorielle de floats est fonctionnel, mais seulement si le float est un entier:
    >>> factorielle(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorielle(30.0)
    265252859812191058636308480000000

    Le nombre passé en factuer ne doit pas etre non plus trop grand:
    >>> factorielle(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
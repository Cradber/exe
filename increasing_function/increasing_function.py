
def find(f, y, a, b):
    """
    Given an increasing function f which takes an integer value n in the range [a, b] and a floating
    point number y; return n if f(n) = y and a <= n <= b, or -1 in another case.

    Args.
    - f: Increasing function taking an integer argument and returning a floating point
    - y: Target floating point
    - a: Lower limit of the search range (inclusive)
    - b: Upper limit of the search range (inclusive)

    Usage:
    ```python
    from mpmath import zetazero # need mpmath installed
    def f(n):
        return 0. if n <= 0 else float(zetazero(n).imag)
    y = f(123456789) # value in the range
    z = y + 1e-8 # value not in the range
    # This should output 123456789 in one or two minutes
    print(find(f, y, 0, 10000000000))
    # This should output -1 in one or two minutes
    print(find(f, z, 0, 10000000000))
    ```
    """

    while a <= b:
        mid = (a + b) // 2
        result = f(mid)

        if result == y:
            return mid
        elif result < y:
            a = mid + 1
        else:
            b = mid - 1

    return -1


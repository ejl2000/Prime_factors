#import doctest


def primefactors(value):
    """
    #>>> value = 15
    #>>> primefactors(value)
    [3, 5]
    #>>> value = 36
    #>>> primefactors(value)
    [2, 2, 3, 3]
    """
    # even number divisible
    divisor = 2
    factors = []
    while divisor * divisor <= value:
        if value % divisor:
            divisor += 1
        else:
            value //= divisor
            factors.append(divisor)
    if value > 1:
        factors.append(value)
    return factors


def convert(factors):
    """
    #>>> factors = [3, 5]
    #>>> convert(factors)
    (3, 5)
    #>>> factors = [2, 2, 3, 3]
    #>>> convert(factors)
    (2, 2, 3, 3)
    """
    return tuple(factors)


def main():
    #doctest.testmod(verbose=True)
    value = "hi"
    factors = []
    try:
        if isinstance(value, int):
            factors = primefactors(value)
        else:
            raise ValueError
    except ValueError:
        print("Please enter an integer")
    #factors = primefactors(value)
    print(tuple(factors))


if __name__ == "__main__":
    main()

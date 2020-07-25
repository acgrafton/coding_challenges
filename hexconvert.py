"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""

    hexadigits = "0123456789ABCDEF"
    hexadict = {}
    digit = 0

    for  char in hexadigits:
        hexadict[char] = digit
        digit += 1

    power = len(hex_in)-1
    decimal = 0
    for char in hex_in:
        decimal += hexadict[char] * 16**power
        power -= 1

    return decimal


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")

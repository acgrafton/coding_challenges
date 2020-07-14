"""Write a function that compresses a string.

Repeated characters should be compressed to one character and the number of
times it repeats:

>>> compress('aabbaabb')
'a2b2a2b2'

If a character appears once, it should not be followed by a number:

>>> compress('abc')
'abc'

The function should handle letters, whitespace, and punctuation:

>>> compress('Hello, world! Cows go moooo...')
'Hel2o, world! Cows go mo4.3'
"""


def compress(string):
    """Return a compressed version of the given string."""

    new_strng = ""       
    count = 1
    for char in string:
        if new_strng and char == new_strng[-1]:
            count +=1
        elif count > 1:
            new_strng = new_strng + str(count) + char
            count = 1
        else:
            new_strng = new_strng + char

    new_strng = new_strng + str(count) if count > 1 else new_strng
    
    return  new_strng
        



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

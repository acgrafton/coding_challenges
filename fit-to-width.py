"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    #split string by spaces into list of words
    #declare variable for printlist pop first word from words 
    #loop through list
    # if length of current word + length of items in print list is less 

    words = string.split()

    fit = [words.pop(0)]
    chars = len(fit[0])

    for word in words:
        if chars + len(word) > limit:
            print(" ".join(fit))
            fit = [word]
            #add one for the space
            chars = len(word) + 1
        else:
            fit.append(word)
            chars += len(word) + 1
    
    if fit: 
        print(" ".join(fit))

    









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')

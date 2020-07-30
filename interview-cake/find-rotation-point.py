"""
 I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

"""


def find_rotation_point(words):
    ALPHABET = 'abcdefghijklmnpqrstuvwxyz'

    first_letter = words[0][0]
    first = 0
    last = len(words) - 1
    
    while len(words) >= 3:
        mid = (last - first) // 2 + first
        before = words[mid-1].lower()
        current = words[mid].lower()
        after = words[mid+1].lower()
        if ALPHABET.index(current[0]) < ALPHABET.index(before[0]):
            return mid
        elif ALPHABET.index(current[0]) > ALPHABET.index(after[0]):
            return mid+1
        elif ALPHABET.index(current[0]) < first_letter:
            last = mid
        elif ALPHABET.index(current[0]) > first_letter:
            first = mid
        

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(find_rotation_point(words))
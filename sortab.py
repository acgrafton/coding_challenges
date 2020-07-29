"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    take first number of each list, compare, and add the lowest to a new list, 
    do the same until one list is empty, and then extend the remaining to the new list

    a = [1, 3, 5, 7]
    b = [2, 6, 8, 10]

    i = 4
    j = 2
    merged_sorted = []

    a[3] = 7
    b[2] = 8
    """

    merge_sorted = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            merge_sorted.append(a[i])
            i += 1
        elif b[j] < a[i]:
            merge_sorted.append(b[j])
            j += 1
        else:
            merge_sorted.append(a[i])
            merge_sorted.append(b[j])
            i += 1
            j += 1

    merge_sorted = merge_sorted + a[i:] + b[j:]

    return merge_sorted




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")

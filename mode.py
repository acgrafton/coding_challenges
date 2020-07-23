"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    mode_dict = {}
    mode = set()

    for num in nums:
        mode_dict[num] = mode_dict.get(num, 0) + 1

    highest = 0
    for num, freq in mode_dict.items():
        if freq == highest:
            mode.add(num)
        elif freq > highest:
            mode.clear()
            mode.add(num)
            highest = freq

    return mode


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")

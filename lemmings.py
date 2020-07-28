"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    if num_holes == len(cafes):
        return 0
    
    furthest = max(abs(cafes[0] - 0), abs(num_holes-cafes[-1]-1))
    
    lower_index = 0
    upper_index = 1

    while len(cafes) > 1 and upper_index < len(cafes):
        distance = (cafes[upper_index] - cafes[lower_index]) // 2
        if distance > furthest:
            furthest = distance
        lower_index = upper_index
        upper_index += 1
    
    return furthest







    
            



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")

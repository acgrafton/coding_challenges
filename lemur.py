"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    jumps = 0
    skipped_branches = 0

    if len(branches) == 1:
        return 0

    if 1 not in branches and len(branches) % 2 == 0:
        return int(len(branches) / 2)

    if 1 not in branches and len(branches) % 2 != 0:
        return (int(len(branches) // 2))

    for i, _ in enumerate(branches):

        if skipped_branches > 0:
            skipped_branches -= 1
            continue

        if i + 2 == len(branches) - 1:
            jumps += 1
            break

        elif branches[i+2] == 1 and (i + 2 == len(branches)-2):
            jumps +=2
            break
        
        elif not branches[i+1] and not branches[i+2]:
            jumps += 1
            skipped_branches = 1

        elif branches[i+2] == 1:
            jumps +=2
            skipped_branches += 2
    
    return jumps

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")
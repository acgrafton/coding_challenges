def merge_ranges(mtg_time_ranges):
    """Given a list of multiple meeting time ranges (tuples), return a list of condensed ranges

    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    
    """

    mtg_time_ranges.sort(reverse=True)

    merged = []

    first_mtg = mtg_time_ranges.pop()
    start = first_mtg[0]
    end = first_mtg[1]

    while mtg_time_ranges:
        
        to_check = mtg_time_ranges.pop()

        if to_check[0] > end:
            merged.append((start, end))
            start = to_check[0]
            end = to_check[1]
        
        else:
            end = to_check[1]

    merged.append((start, end))

    return merged
        
if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print("success!")

    


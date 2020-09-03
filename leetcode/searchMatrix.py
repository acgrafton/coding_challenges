"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:


    >>> searchMatrix([[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
    True

    >>> searchMatrix([[1, 3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]], 13)
    False


Implementation Notes: Check if target is between first and last elements of each row to determine which row it is in. Use binary search on the row to find if it is in it or not.
Runtime: O(m log n) => Worse case check all rows and half of all elements in target row.
Memory: O(1)

"""

def searchMatrix(matrix, target):
        
        for row in matrix:
            
            if not row: break
            
            if row[0] <= target <= row[len(row)-1]:

                floor = 0
                ceiling = len(row)-1
                while floor <= ceiling:
                    i = ((ceiling - floor) // 2) + floor
                    if target in (row[floor], row[i], row[ceiling]):
                        return True
                    elif row[floor] < target < row[i]:
                        ceiling = i-1
                    else:
                        floor = i+1
        return False

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    #loop through the matrix:
        #if 0 is in the list, loop through list and if item is not 0, change to 0 else get the index
        #loop back through and if 0 is not in the list, add a 0 to the saved index
        #return matrix
    
    row_index = None
    
    #loop through matrix 
    for i, row in enumerate(matrix):

        #if there is a 0 in the row, loop through that row
        if 0 in row:
            for i2, item in enumerate(row):
                if item == 0:
                    row_index = i2
                else:
                    row[i2] = 0
            col_index = i
    
            while col_index != 0:
                col_index -= 1
                matrix[col_index][row_index] = 0
            continue
        
        if row_index is not None:
            row[row_index] = 0

    return matrix

    


    
    



        
                    
                
            


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")

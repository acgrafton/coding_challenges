def spiralOrder(matrix):
  
  spiral = []
  seen = set()

  try:
    total_nums = len(matrix) * len(matrix[0])
    row_start, row_end = 0, len(matrix)-1
    col_start, col_end = 0, len(matrix[0])-1

    while (row_start, col_start) not in seen:
      curr_row, curr_col = row_start, col_start
      # print('add', curr_row, curr_col, matrix[curr_row][curr_col])
      spiral.append(matrix[curr_row][curr_col])
      seen.add((curr_row, curr_col))
      while curr_col < col_end and len(seen) != total_nums:
          curr_col += 1
          # print('add', curr_row, curr_col, matrix[curr_row][curr_col])
          spiral.append(matrix[curr_row][curr_col])
          seen.add((curr_row, curr_col))
      while curr_row < row_end and len(seen) != total_nums:
          curr_row += 1
          # print('add', curr_row, curr_col, matrix[curr_row][curr_col])
          spiral.append(matrix[curr_row][curr_col])
          seen.add((curr_row, curr_col))
          
      while curr_col > col_start and len(seen) != total_nums:
          curr_col -= 1
          # print('add', curr_row, curr_col, matrix[curr_row][curr_col])
          spiral.append(matrix[curr_row][curr_col])
          seen.add((curr_row, curr_col))
          
      while curr_row-1 > row_start and len(seen) != total_nums:
          curr_row -= 1
          # print('add', curr_row, curr_col, matrix[curr_row][curr_col])
          spiral.append(matrix[curr_row][curr_col])
          seen.add((curr_row, curr_col))
          
      row_start += 1
      row_end -= 1
      col_start += 1
      col_end -= 1
    # print(seen)

  except:
    pass
  
  return spiral
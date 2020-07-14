def asterisk(word):
    """Return a word in asterisks leaving punctuation intact."""

    punctuation = '!\"#$%&\'()+, -./:;<=>?@[\]^_`{|}~'
    censored = []
    
    #Loop through each character in the word, if it's a punctuation, leave in place, otherwise, replace with a *. 
    for char in word:
        if char in punctuation:
            censored.append(char)
        else:
            censored.append('*')
    
    return "".join(censored)


def censor(unwanted_words, message):

    words = message.split()

    for unwanted_word in unwanted_words:

        if "*" not in unwanted_word and unwanted_word not in words:
            continue

        stripped_word = unwanted_word.strip('*').lower() if '*' in unwanted_word else unwanted_word.lower()
        
        for i, word in enumerate(words):
            if stripped_word in word.lower():
                words[i] = asterisk(word)

    return " ".join(words)


message = "I drove down into the city to see some cherries falling in the sky but then some mean birds created some incidents."
unwanted_words = ['in*','city', 'mean'] 

print(censor(unwanted_words, message))

def find_center(matrix):
    """Given a square matrix, return a tuple of the row and column index"""
    
    if len(matrix) % 2 == 0:
        return (int(len(matrix)/2 - 1), int(len(matrix)/2 - 1))
    else:
        return (int(len(matrix)//2), int(len(matrix)//2))


def get_points_to_check(point, matrix):
    """Return a list of valid points to check (top, left, bottom, right)"""

    row = point[0]
    col = point[1]

    points = []

    if row - 1 >= 0:
        points.append((row-1, col))

    if row + 1 < len(matrix):
        points.append((row+1, col))

    if col - 1 >= 0:
        points.append((row, col-1))

    if col + 1 < len(matrix):
        points.append((row, col+1))

    return points

def get_highest(point, matrix):
    """Given a list of points and a matrix, return point with the highest value of its neighbors"""

    highest_val = 0
    highest_coord = (0,0)

    points = get_points_to_check(point, matrix)

    for row, col in points:

        if matrix[row][col] > highest_val:
            highest_val = matrix[row][col]
            highest_coord = (row, col)
    
    return highest_coord if highest_val > 0 else None


def traverse_highest(matrix):

    point = find_center(matrix)
    curr_row = point[0]
    curr_col = point[1]

    while True:
        matrix[curr_row][curr_col] = 0
        point = get_highest(point, matrix)
        
        if point is None:
            break
        
        curr_row = point[0]
        curr_col = point[1]

    sum = 0
    for row in matrix:
        for val in row:
            sum += val

    return sum

first_ex = [[1,0,8,20],[7,4,9,21],[2,3,7,11],[4,6,8,14]]
print(traverse_highest(first_ex))



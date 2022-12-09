import numpy as np

##### PART TWO

def check_column(matrix, row_index, column_index, el):
    column = matrix[:, column_index]

    limit = len(column)

    up = 1
    down = 1

    flag_up = False if row_index != 0 else True
    flag_down = False if row_index != limit-1 else True

    n_trees_up = 0
    n_trees_down = 0

    while flag_down == False or flag_up == False:

        if row_index - up < 0:
            flag_up = True

        if row_index + down >= limit:
            flag_down = True

        if flag_up == False:
            n_trees_up += 1
            if column[row_index - up] >= el:
                flag_up = True
            else:
                up += 1
        
        if flag_down == False:
            n_trees_down += 1
            if column[row_index + down] >= el:
                flag_down = True
            else:
                down +=1

    n_trees_up = 1 if n_trees_up == 0 else n_trees_up
    n_trees_down = 1 if n_trees_down == 0 else n_trees_down

    print(f"UP AND DOWN {n_trees_up}, {n_trees_down}")
    return n_trees_up*n_trees_down

        


def check_row(matrix, row_index, column_index, el):
    row = matrix[row_index, :]

    limit = len(row)

    left = 1
    right = 1

    flag_left = False if column_index != 0 else True
    flag_right = False if column_index != limit-1 else True

    n_trees_left = 0
    n_trees_right = 0

    while flag_left == False or flag_right == False:

        if column_index - left < 0:
            flag_left = True

        if column_index + right >= limit:
            flag_right = True

        if flag_left == False:
            n_trees_left += 1
            if row[column_index - left] >= el:
                flag_left = True
            else:
                left += 1
        
        if flag_right == False:
            n_trees_right += 1
            if row[column_index + right] >= el:
                flag_right = True
            else:
                right +=1

    n_trees_left = 1 if n_trees_left == 0 else n_trees_left
    n_trees_right = 1 if n_trees_right == 0 else n_trees_right
    print(f"LEFT AND RIGHT {n_trees_left}, {n_trees_right}")
    return n_trees_right*n_trees_left

with open("./Day08/input.txt", "r", encoding = 'utf-8') as f:
    
    rows = f.readlines()

    forest = []
    
    for row in rows:
        matrix_row = []
        for char in row:
            if char != '\n':
                matrix_row.append(int(char))

        forest.append(matrix_row)
        
f.close()

forest = np.array(forest)

n_visible = 0

result = []

n_rows, n_cols = forest.shape

for i, row in enumerate(forest):
    for j, el in enumerate(row):
        el = forest[i][j]
        r = check_row(forest, i, j, el)*check_column(forest, i, j, el)
        result.append(r)


print(f"MAX: {max(result)}")
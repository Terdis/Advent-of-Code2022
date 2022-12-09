import numpy as np

##### PART ONE


def check_column(matrix, row_index, column_index, el):
    return (sum(matrix[:row_index, column_index] >= el) == 0 or sum(matrix[row_index+1:, column_index] >= el) == 0)

def check_row(matrix, row_index, column_index, el):
    return (sum(matrix[row_index, :column_index] >= el) == 0 or sum(matrix[row_index, column_index+1:] >= el) == 0)


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

n_rows, n_cols = forest.shape

for i, row in enumerate(forest):
    for j, el in enumerate(row):

        if (i != 0 and j != 0 and i != n_rows-1 and j != n_cols-1):
            if check_column(forest, i, j, el) or check_row(forest, i, j, el):
                n_visible += 1

        else:
            n_visible += 1

            

print(f"VISIBLE TREES: {n_visible}")


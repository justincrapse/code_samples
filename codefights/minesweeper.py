"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have
a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement
of mines we want to create a Minesweeper game setup.
input:
[[True,False,False,True],
 [False,False,True,False],
 [True,True,False,True]]
output:
[[0,2,2,1],
 [3,4,3,3],
 [1,2,3,1]]
 """


def minesweeper(matrix):
    m_list = matrix[:]
    matrix = [[False] + i + [False] for i in matrix]
    matrix.append([False for i in matrix[0]])
    matrix.insert(0, [False for i in matrix[0]])
    new_matrix = []
    for i1, v1 in enumerate(m_list):
        new_row = []
        for i2, v2 in enumerate(v1):
            pixels = [i[i2:i2 + 3] for i in matrix[i1:i1 + 3]]
            pixels[1][1] = False
            new_row.append(int(sum([sum(i) for i in pixels])))
        new_matrix.append(new_row)
    return new_matrix


matrix_in = [
    [True, False, False, True],
    [False, False, True, False],
    [True, True, False, True]
]

print(*minesweeper(matrix_in), sep='\n')

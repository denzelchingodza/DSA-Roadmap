# Given an m x n matrix where each row is sorted left to right, and the first
# number of each row is greater than the last number of the row above it,
# determine whether a given target value exists anywhere in the matrix.

def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = mid // cols, mid % cols
        value = matrix[row][col]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

"""
THE PICTURE: imagine tearing every row of the grid off and taping them end
to end into one long strip of paper. Because of how the matrix is built
(each row sorted, and the first number of a row is bigger than the last
number of the row above), that strip is fully sorted, start to finish.
We never actually tear the paper -- we just do the math to figure out,
for any position on the imagined strip, which row and column that
position would have landed on.

Why mid // cols and mid % cols work: mid // cols tells you how many FULL
rows fit before reaching position mid (that's your row number), and
mid % cols tells you how far into that row you are (your column). Same
idea as converting a seat number on a bus into "row number, seat within
that row" when every row has the same number of seats.

TRACE IT:
matrix = [[1,3,5],[7,10,12],[15,17,19]], target = 10
rows=3, cols=3 -> flat positions 0..8 represent the strip
[1,3,5,7,10,12,15,17,19]

left=0, right=8 -> mid=4 -> row=4//3=1, col=4%3=1 -> matrix[1][1]=10
-> matches target -> return True

If it hadn't matched right away (say target=17): keep narrowing left/right
exactly like ordinary binary search, always converting the current mid
back into a real (row, col) before comparing.
"""

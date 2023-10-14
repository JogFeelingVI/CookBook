用python写一个解答数独的程序这是一个使用回溯算法来解决数独问题的Python程序：

```python
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

# 测试数独
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

print_board(board)
solve(board)
print("___________________")
print_board(board)
```

这个程序首先定义了一个solve函数，它接受一个数独板（2D列表）作为参数。如果板上没有空的位置，那么数独已经解决，函数返回True。否则，它找到一个空的位置，并尝试在那个位置放置1-9的每个数字。如果数字有效（即它不违反数独的规则），那么它将数字放在那个位置，并递归地尝试解决板。如果后续的递归调用返回True，那么数独已经解决，函数返回True。否则，它撤销放置的数字，并继续尝试下一个数字。如果它已经尝试了所有的数字，但没有一个是有效的，那么数独无解，函数返回False。
https://cloud.tencent.com/developer/ask/sof/106561696/answer/117504862

http://www.sudocue.net/guide.php#NakedSingle
'''
by gitHub account: jpsvcv

Sudoku - Finally I'd learned how Sudoku works

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
YES

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
NO
'''

def print_message(msg):
    print(msg)


def decrease_row_count(row):

    if row > 0:
        return row - 1


def input_test_data(option):
    if option == 0:
        board.append(list('295743861'))
        board.append(list('431865927'))
        board.append(list('876192543'))
        board.append(list('387459216'))
        board.append(list('612387495'))
        board.append(list('549216738'))
        board.append(list('763524189'))
        board.append(list('928671354'))
        board.append(list('154938672'))
    elif option == 1:
        board.append(list('195743862'))
        board.append(list('431865927'))
        board.append(list('876192543'))
        board.append(list('387459216'))
        board.append(list('612387495'))
        board.append(list('549216738'))
        board.append(list('763524189'))
        board.append(list('928671354'))
        board.append(list('254938671'))
    return board


def read_data():
    row = 0
    while row < 9:
        print('Input row No.', row + 1, ':', end=' ')
        try:
            row_data = int(input())
            if len(str(row_data)) > 9:
                print('To long, please try again')
                row = decrease_row_count(row)
            elif len(str(row_data)) < 9:
                print('To short, please try again')
                row = decrease_row_count(row)
            else:
                row_data = str(row_data)
                board.append(list(row_data))
        except ValueError:
            print('Only Integers are acceptable. Please try again.')
            row = decrease_row_count(row)
        row += 1
    return board


def print_board():
    print()
    row = 0
    for it in main_board:
        col = 0
        for i in it:
            if col == 2 or col == 5:
                print(i, '\t|', end='\t')
            else:
                print(i, end='\t')
            col += 1
        if row == 2 or row == 5:
            print()
            print('-' * 41)
        else:
            print()
        row += 1


def list_str2int():
    tmp_board = []
    for row in board:
        tmp_board.append([int(st) for st in row])
    return tmp_board


def create_sub_squares():
    cell = line = 0
    for row in main_board:
        pos = 0
        for col in row:
            if pos <= 2:  # 1st cell of the row
                sub_lists[cell].append(col)
            elif 2 < pos < 6:  # 2nd cell of the row
                sub_lists[cell].append(col)
            else:  # 3rd cell of the row
                sub_lists[cell].append(col)
            if pos == 2 or pos == 5:
                cell += 1
            pos += 1
        cell = 0
        line += 1
        if 6 > line > 2:  # 4th cell of the row
            cell = 3
        elif line > 5:  # 5th cel of the row
            cell = 6
    return sub_lists


def compute_list(data):
    for row in data:
        if sorted(row) != test_data:
            return False
    return True


# 2a) - Check the Main row
def compute_row():
    return compute_list(main_board)


# 2b) - Check the Main column
def compute_col():
    index = 0
    while index < 9:
        tmp_col = test_data[:]
        for col in main_board:
            for col_item in col:
                if col[index] == col_item:  # get the right position
                    if col_item not in test_data:
                        return False
                    else:
                        tmp_col.remove(col_item)
                        break
        if len(tmp_col) > 0:
            return False
        index += 1
    return True


# 2c) - Check the sub_squares
def compute_squares():
    return compute_list(sub_squares)


board = []
test_data = [x for x in range(1, 10)]

# print(read_data(board))
for i in range(2):
    # 1 - Board and Sub_squares building process
    board = input_test_data(i)
    main_board = list_str2int()
    print_board()
    sub_lists = [[] for i in range(9)]
    sub_squares = create_sub_squares()

    # 2 - Compute the Table [row, column, squares]
    if compute_row() and compute_squares():
        if compute_col():
            print('\nYes')
    else:
        print('\nNo')

    # reset
    board = main_board = sub_lists = sub_squares = []
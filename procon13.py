# coding:utf-8


def solve(n, m, M):
    matrix = []
    for target_int in range(1, n+1):
        mylist = []
        mylist.append(target_int)

        for max in range(2, n+1):
            if max > target_int:
                continue
            elif max == target_int:
                mylist.append(1)
                continue
            else:
                mylist.append([target_int-max, max])
        matrix.append(mylist)

    print(matrix)
    target_row = matrix[n-1]
    print(target_row)

    for i in target_row:
        A_counter = 0
        num = 0
        if isinstance(i, int):
            counter = i
        else:
            row = i[0]
            column = i[1]
            next_row = matrix[row]
            if column > row:
                '超えてる'
            else:
                target_data = next_row[column]





solve(5, 3, 2)


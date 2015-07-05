# coding:utf-8

def solve(n, m, M):
    matrix = [[[1]]]
    for row_num in range(2, n+1):
        row = []
        for column_num in range(1, row_num+1):
            rem = row_num - column_num
            if column_num > 1:
                target1 = matrix[row_num - 2][column_num - 2]
            else:
                target1 = []
            if rem >= column_num:
                target2 = matrix[rem-1][column_num-1]
                newtarget2 = []
                if len(target2) >= 1:
                    for el in target2:
                        if el < m:
                            newtarget2.append(el+1)
            else:
                newtarget2 = []
            mylist = target1 + newtarget2
            row.append(mylist)
        matrix.append(row)
        print(row)

    target_row = matrix[n-1]
    counter = 0
    for mylist in target_row:
        counter += len(mylist)
    print(counter%M)


solve(10, 5, 1)

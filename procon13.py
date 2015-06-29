# coding:utf-8

<<<<<<< HEAD
def solve(n, m, M):
    matrix = []
    for row_num in range(1, n+1):
        row = []
        for column_num in range(1, row_num+1):
            rem = row_num - column_num
            counted_num_list = []
            if rem == 0:
                counted_num_list = [1]
            else:
                target_row = matrix[rem-1]
                l = 0
                if rem <= column_num:
                    l = rem
                else:
                    l = column_num

                for h in range(l):
                    el_list = target_row[h][1]
                    if len(el_list) >= 1:
                        for num in el_list:
                            if num < m:
                                counted_num_list.append(num+1)
            tuple = (rem, counted_num_list)
            row.append(tuple)
        matrix.append(row)
        print(row)
    target = matrix[n-1]
    counter = 0
    for el in target:
        mylist = el[1]
        counter += len(mylist)
    print(counter%M)



solve(6, 6, 4)


=======

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
>>>>>>> 5dc465bd7c4710d17f506ae9bcb5fe2d64126ba7


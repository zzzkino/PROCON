# coding:utf-8

def solve(n, m, a_list, M):
    preRow = [0 for _ in range(m+1)]
    preRow[0] = 1
    row = preRow[:]
    for i in range(n):
        a = a_list[i]
        row[0] = 1
        for k in range(1, m+1):
            c = 0
            if k-a-1 >= 0:
                c = preRow[k-a-1]
            row[k] = (preRow[k] + row[k-1] - c + M)%M
        #print(row)
        preRow, row = row, preRow;
    answer = preRow[m]
    print(answer)


solve(4, 5, [2, 1, 3, 2], 100)  # n=3 m=3 a=[1,3,2] M=100


solve(1000, 1000, [1000 for i in range(1000)], 10000)






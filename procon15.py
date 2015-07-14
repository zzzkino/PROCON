# coding:utf-8

def solve(n, m, a_list, M):
    matrix = [[1]]
    for i in range(n):
        a = a_list[i]
        PreRow = matrix[i]
        LenPreRow = len(PreRow)
        Row = [1]
        LenRow = len(PreRow) + a
        if LenRow > m+1:
            LenRow = m+1
        for k in range(1, LenRow):
            b = 0
            c = 0
            if LenPreRow >= k+1:
                b = PreRow[k]
            if k-a-1 >= 0:
                c = PreRow[k-a-1]
            el = b + Row[-1] - c
            Row.append(el)
        print(Row)
        matrix.append(Row)
    answer = matrix[-1][-1]%M
    print(answer)


solve(4, 5, [2, 1, 3, 2], 100)  # n=3 m=3 a=[1,3,2] M=100


solve(1000, 1000, [1000 for i in range(1000)], 1000)






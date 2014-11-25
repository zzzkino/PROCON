dic={'A':1, 'B':2, 'C':3, 'D':4, 'E':5,
    'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
    'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
    'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
    'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

def charT(N,S):
    i = 0
    T = ''
    while i < N:
        if dic[S[0]] > dic[S[-1]]:
            T = T + S[-1]
            S = S[:-1]
            i += 1
        elif dic[S[0]] < dic[S[-1]]:
            T = T + S[0]
            S = S[1:]
            i += 1
        else:
            i += 1
            SS = S
            if len(SS) > 3:
                while dic[SS[0]] == dic[SS[-1]]:
                    SS = SS[1:-1]
                    if len(SS) < 3:
                        break
                if dic[SS[0]] > dic[SS[-1]]:
                    T = T + S[-1]
                    S = S[:-1]
                else:
                    T = T + S[0]
                    S = S[1:]
            else:
                T = T + S[0]
                S = S[1:]
    print(T)

N = 8
S = 'ABFCAFCA'
charT(N,S)

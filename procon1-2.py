def X(mai,en,A):
    a = int(A / en)
    if mai >= a:
        return a
    else:
        return mai

def coin(c1,c5,c10,c50,c100,c500,A):
    count = 0
    lista = [c500,c100,c50,c10,c5,c1]
    listb = [500,100,50,10,5,1]
    for i in range(6):
        a = X(lista[i],listb[i],A)
        count += a
        A = A-listb[i]*a
    return count

print(coin(3,2,1,3,0,2,622))



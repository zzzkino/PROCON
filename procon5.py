def counter(N,L):
    counter = 0
    for i in range(N-1):
        L.sort()
        X = L.pop(0)
        Y = L.pop(0)
        counter += X+Y
        L.append(X+Y)
        print(L)
        print(counter)

N = 3
L = [8,5,8]
counter(N,L)

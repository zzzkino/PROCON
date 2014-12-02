def pointcounter(N,R,X):
    counter = 0
    point = 0
    for left in range(N):
        if point <= left:
            for right in range(left +1,N):
                if X[right]-X[left] > R:
                    point = right -1
                    counter += 1
                    break
    print(counter)




N = 6
R = 10
X = [1,7,15,20,30,50]
pointcounter(N,R,X)

for i in range(1,6):
    print(i)
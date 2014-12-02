def pointcounter(N,R,X):
    counter = 0
    point = 0
    for left in range(N):
        if point <= X[left]:
            if left == N-1:
                counter += 1
                break
            for right in range(left +1,N):
                if X[right]-X[left] > R:
                    point = X[right -1] +R
                    print('point;')
                    print(point)
                    counter += 1
                    break
    print(counter)




N = 6
R = 10
X = [0,0,1,3,15,29]
pointcounter(N,R,X)

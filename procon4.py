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
                    counter += 1
                    break
    print(counter)

N = 6
R = 1
X = [0,1,2,3,15,16]
pointcounter(N,R,X)

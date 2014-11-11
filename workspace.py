#coding:utf-8

def work(n,s,t):
    Count1 = 0
    Count2 = 1
    a = min(t)
    while Count1 < n:
        listA = [i for i,j in enumerate(s) if j > a]
        listB = []
        if a < max(s):
            Count2 += 1
            for i in listA:
                listB.append(t[i])
                a = min(listB)
            print listB
        Count1 += 1
    print 'answer:'+ str(Count2)

n=7
s=[1,5,3,2,6,8,7]
t=[2,6,4,4,7,9,10]
work(n,s,t)

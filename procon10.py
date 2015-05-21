input=raw_input()
a=input
a=a.split(' ')
mylist=[int(a[2])-int(a[0]),int(a[4])-int(a[0])]
mylist2=[int(a[3])-int(a[1]),int(a[5])-int(a[1])]
b=float(mylist[0]*mylist2[1]-mylist[1]*mylist2[0])
if b<0:
    b=-b

print(float(b/2))

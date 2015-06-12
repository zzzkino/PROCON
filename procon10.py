<<<<<<< HEAD
input=raw_input()
a=input
a=a.split(' ')
mylist=[int(a[2])-int(a[0]),int(a[4])-int(a[0])]
mylist2=[int(a[3])-int(a[1]),int(a[5])-int(a[1])]
b=float(mylist[0]*mylist2[1]-mylist[1]*mylist2[0])
if b<0:
    b=-b

print(float(b/2))
=======

def solve(list_of_target_list, target_weight):
    new_list = [x for x in list_of_target_list if x[0] <= target_weight]
    values = {0: 0}
    for mylist in new_list:
        myweight = mylist[0]
        myvalue = mylist[1]
        new_values = values.copy()
        for value, weight in values.items():
            if weight + myweight <= target_weight:
                a = values.get(value + myvalue, -1)
                if a == -1 or a > myweight + weight:
                    new_values[value + myvalue] = myweight + weight
        values = new_values
        print(values)
    answer = max(values.keys())
    print('Answer is '+str(answer))


test = [[2, 3], [5, 6], [4, 5], [3, 2]]  #(w,v)

# solve([[i,i] for i in range(1,100)], 10000)

solve(test,13)


>>>>>>> 652a405211631a462d6e890a679a56f268c282d0

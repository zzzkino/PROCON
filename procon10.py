
def solve(list_of_target_list, target_weight):
    new_list = [x for x in list_of_target_list if x[0] <= target_weight]
    print(new_list)
    values = {0:0}
    for mylist in new_list:
        myweight = mylist[0]
        myvalue = mylist[1]
        new_values = values.copy()
        for value, weight in values.items():
            if weight + myweight <= target_weight:
                a=values.get(value + myvalue, -1)
                if a == -1 or a > myweight + weight:
                    new_values[value + myvalue] = myweight + weight
        values = new_values
        print(values)
    anser = max(values.keys())
    print('Anser is '+str(anser))


test = [[2, 3], [5, 6], [4, 5], [3, 2]]  #(w,v)

# solve([[i,i] for i in range(1,100)], 10000)

solve(test,13)



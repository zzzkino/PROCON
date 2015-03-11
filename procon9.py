def solve(listoflist, target_weight):
    new_list = sorted([x for x in listoflist if x[0] <= target_weight], key=lambda x:x[0], reverse=True)
    print(new_list)
    weights = {0: 0}
    for mylist in new_list:
        myweight = mylist[0]
        myvalue = mylist[1]
        new_weights = weights.copy()
        for weight, value in weights.items():
            counter = 1
            while weight + myweight * counter <= target_weight:
                if weights.get(weight + myweight*counter, 0) < value + myvalue:
                    new_weights[weight + myweight*counter] = value + myvalue
                    counter += 1
                else:
                    counter += 1
        weights = new_weights
        print(weights)
    anser = max(weights.values())
    print('Anser is '+str(anser))


test = [[2, 3], [5, 6], [4, 5], [3, 2]]  #(w,v)

solve([[i,i] for i in range(1,100)], 10000)

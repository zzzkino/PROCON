<<<<<<< HEAD:procon9.py
def solve(listoflist, target_weight):
    new_list = sorted([x for x in listoflist if x[0] <= target_weight], key=lambda x:x[0], reverse=True)
=======
def solve(list_of_target_list, target_weight):
    new_list = [x for x in list_of_target_list if x[0] <= target_weight]
>>>>>>> 4dceba49e31facf9bfddeab1ca371a0d6ab43c4a:procon9
    print(new_list)
    weights = {}
    for i in range(target_weight+1):
        weights[i] = 0
    for mylist in new_list:
        myweight = mylist[0]
        myvalue = mylist[1]
        new_weights = weights.copy()
        for weight, value in weights.items():
            if weight + myweight <= target_weight:
                if weights.get(weight + myweight, 0) < value + myvalue:
                    new_weights[weight + myweight] = value + myvalue
        weights = new_weights
        print(weights)
    anser = max(weights.values())
    print('Anser is '+str(anser))


test = [[2, 3], [5, 6], [4, 5], [3, 2]]  #(w,v)

solve([[i,i] for i in range(1,100)], 10000)


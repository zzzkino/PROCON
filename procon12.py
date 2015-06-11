
def solve(target_list):
    dic = {0: 0}
    for num in target_list:
        new_dic = dic.copy()
        for key_counter, value_num in dic.items():
            if value_num < num:
                if (key_counter + 1 not in dic):
                    new_dic[key_counter + 1] = num
                elif dic[key_counter + 1] > num:
                    new_dic[key_counter + 1] = num
                else:
                    pass
        dic = new_dic
        print(dic)

    max_counter = max(dic.keys())
    print(max_counter)


solve([1,3,8,3,12,14,11,5])

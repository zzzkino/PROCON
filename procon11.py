def solve(k, target_list):
    values_dic = {0: 1}
    criteria = 'NG'
    for mylist in target_list:
        val = mylist[0]
        num = mylist[1]
        new_values_dic = values_dic.copy()
        for value_key in values_dic.keys():
            for i in range(1, num+1):
                new_value = value_key + val*i
                if new_value == k:
                    criteria = 'OK'
                    break
                elif new_value < k:
                    new_values_dic[new_value] = 1
                else:
                    break
            if criteria == 'OK':
                break
        if criteria == 'OK':
            break
        values_dic = new_values_dic
    print(criteria)

solve(17, [[3, 5], [5, 4], [13, 2]])

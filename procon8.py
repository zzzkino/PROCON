
def make_listoflist(char1, char2):
    min_char = ''
    max_char = ''
    large_list = []
    if len(char1) < len(char2):
        min_char = char1
        max_char = char2
    else:
        min_char = char2
        max_char = char1
    for char in min_char:
        counter = 0
        small_list = []
        for target_char in max_char:
            if char == target_char:
                small_list.append(counter)
                counter += 1
            else:
                counter += 1
        large_list.append(small_list)
    return large_list


def find_maxnum_and_cahnge_listoflist(listoflist):
    max_list = []
    newlistoflist = []
    for i in range(len(listoflist)):
        if listoflist[i] != []:
            max_list.append(max(listoflist[i]))
            newlistoflist.append(listoflist[i])
    listoflist = newlistoflist
    return [max(max_list), listoflist]


def solve(listoflist):
    max_num = find_maxnum_and_cahnge_listoflist(listoflist)[0]
    listoflist = find_maxnum_and_cahnge_listoflist(listoflist)[1]
    box = [(-1,0)]
    for i in range(max_num+1):
        box.append((i))
    for list in listoflist:
        for tuple in box:
            if len(tuple) == 2:
                for el in list:
                    if tuple[0] < el:
                        box.append(el, tuple[1]+1)
                    



s = 'aiyd'
t = 'aiudadf'
print(make_listoflist(s, t))
find_maxnum(make_listoflist(s, t))

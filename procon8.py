
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


def change_listoflist(listoflist):
    newlistoflist = []
    for i in range(len(listoflist)):
        if listoflist[i] != []:
            newlistoflist.append(listoflist[i])
    listoflist = newlistoflist
    return listoflist


def solve(listoflist):
    listoflist = change_listoflist(listoflist)
    box = [(-1, 0)]
    print(listoflist)
    for list in listoflist:
        new_box = []
        for tuple in box:
            for el in list:
                if tuple[0] < el:
                    new_box.append((el, tuple[1]+1))
                    break
        box.extend(new_box)
        box = sorted(box, key=lambda x:x[0])
        cal_list = []
        for i in range(len(box)-1):
            for k in range(i+1, len(box)):
                if box[i][0] == box[k][0]:
                    if box[i][1] <= box[k][1]:
                        cal_list.append(i)
                        break
        cal_list.sort()
        cal_list.reverse()
        for i in cal_list:
            del box[i]
        print(box)

    box=sorted(box, key=lambda x:x[1], reverse=True)
    print('答えは'+str(box[0][1]))
                    

s = 'aifydgfii'
t = 'aiudadf'
solve(make_listoflist(s, t))


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
    box = [(-1, 0)]
    for list in listoflist:
        newbox = box
        for tuple in box:
            print(tuple)
            for el in list:
                if tuple[0] < el:
                    newbox.append((el, tuple[1]+1))
                    # print(newbox)
                    break
        newbox=sorted(newbox, key=lambda x:x[0])
        cal_list=[]
        print('bb')
        for i in range(len(newbox)-1):
            for k in range(i+1, len(newbox)-1):
                if newbox[i][0] == newbox[k][0]:
                    if newbox[i][1] <= newbox[k][1]:
                        cal_list.append(i)
                        break
        cal_list.sort()
        cal_list.reverse()
        # print(cal_list)
        for i in cal_list:
            del newbox[i]
        # print(newbox)
        box = newbox
    box=sorted(box, key=lambda x:x[1], reverse=True)
    print('答えは'+str(box[0][1]))
                    

s = 'aiyd'
t = 'aiudadf'
print(make_listoflist(s, t))
solve(make_listoflist(s, t))


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


def countsubsequence(listoflist):
    counter = 0
    memo = -1
    for i in range(len(listoflist)):
        for num in listoflist[i]:
            if memo < num:
                memo = num
                counter +=1
                break
        print(memo)
    print('答えは'+str(counter))


s = 'aiyd'
t = 'aiudadf'
print(make_listoflist(s, t))
countsubsequence(make_listoflist(s, t))

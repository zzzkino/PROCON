def get_max_value(list,W):
    note=[(0,0)] #memoの２つのtupleをもとからあるnoteの要素に足したもの
    note2=[] #noteのweightでだぶったものを消したnote
    note3=[]
    note4=[]
    memo=[]
    memo2=[]
    for tuple in list:
        weight=tuple[0]
        value=tuple[1]
        if weight <= W:
            for i in note:
                note2.append(i)
                note2.append((i[0]+ weight,i[1]+ value ))
            for i in note2:
                if i[0]<=W:   #重さの超えたものを捨てる
                    note3.append(i)
            sortednote3=sorted(note3, key=lambda x:x[0],reverse=True) #重さが大きい順
            x=len(sortednote3)
            i=0
            while i < x-1:
                if sortednote3[i][0]==sortednote3[i+1][0]:
                    if sortednote3[i][1]>sortednote3[i+1][1]:
                        memo.append(i+1)
                        i+=1
                    else:
                        memo.append(i)
                        i+=1
                i+=1
            memo.sort()
            memo.reverse()#大きい順
            for n in memo:
                sortednote3.pop(n)
            memo=[]
            note=sortednote3
            note2=[]
            note3=[]

    sorted(note, key=lambda x:x[1],reverse=True)#価値が大きい順
    print(note)
    print(note[0][1])


#(w,v)
list=[(5,4),(2,3),(2,4),(4,2),(2,1)]
get_max_value(list,10)

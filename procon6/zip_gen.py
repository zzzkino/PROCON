File = open('ziptest')
text = File.read()
File.close()
print(text)
CharCountDict = {}
for char in text:
    if char in CharCountDict:
        CharCountDict[char] = CharCountDict[char] + 1
    else:
        CharCountDict[char] = 1
CharCountTuple = CharCountDict.items()

ListOfCharLists = []
Charlist=[]
for tuple in CharCountTuple:
    ListOfCharLists.append([tuple[1],tuple[0]])
    Charlist.append(tuple[0])

CharCodeDict={}
def make_CharCodeDict(List):
    n = len(List)
    for i in range(n-1):
        sorted(List, key=lambda x:x[0])
        X = List.pop(0)
        Y = List.pop(0)
        x=len(X)
        y=len(Y)
        newlist=[X[0]+Y[0]]
        for k in range(x-1):
            newlist.append(X[k+1])
            if X[k+1] in CharCodeDict:
                CharCodeDict[X[k+1]]='0'+CharCodeDict[X[k+1]]
            else:
                CharCodeDict[X[k+1]]='0'
        for l in range(y-1):
            newlist.append(Y[l+1])
            if Y[l+1] in CharCodeDict:
                CharCodeDict[Y[l+1]]='1'+CharCodeDict[Y[l+1]]
            else:
                CharCodeDict[Y[l+1]]='1'
        List.append(newlist)
make_CharCodeDict(ListOfCharLists)

CodeCharDict={}
def make_CodeCharDict(List):
    for char in List:
        CodeCharDict[CharCodeDict[char]]=char
make_CodeCharDict(Charlist)

text_zip = ''
for char in text:
    text_zip = text_zip + CharCodeDict[char]
print(text_zip)

newtext = ''
disc = ''
for code in text_zip:
    disc = disc + code
    char = CodeCharDict.get(disc, 'null')
    if char != 'null':
        newtext = newtext + char
        disc=''
print(newtext)

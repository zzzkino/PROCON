File=open('ziptest')
text=File.read()
File.close()
print(text)
chardict={}
for char in text:
    if char in chardict:
        chardict[char]=chardict[char]+1
    else:
        chardict[char]=1
CharCountTuple=chardict.items()
SortedCharCountTuple=sorted(CharCountTuple, key=lambda x:x[1],reverse=True)
SortedCharList=[]
for tuple in SortedCharCountTuple:
    SortedCharList.append(tuple[0])
n=len(SortedCharList)
list_01=[]
for i in range(0,n):
    code_01=''
    code_01=code_01+'1'*i+'0'
    list_01.append(code_01)
CharCodeDict={}
CodeCharDict={}
for i in range(0,n):
    CharCodeDict[SortedCharList[i]]=list_01[i]
    CodeCharDict[list_01[i]]=SortedCharList[i]
# print(CharCodeDict)
# print(CodeCharDict)
text_zip=''
for char in text:
    text_zip=text_zip+CharCodeDict[char]
print(text_zip)


newtext=''
while len(text_zip) !=0:
    A='0'
    while text_zip[0]=='1':
        text_zip=text_zip[1:]
        A='1'+A
    newtext= newtext + CodeCharDict[A]
    text_zip=text_zip[1:]
print(newtext)

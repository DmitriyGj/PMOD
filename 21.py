text = open('text.txt','r',encoding='UTF-8')
string=str(text.readline())
res=str()
letter=0
for i in range(1,len(string)):
    if(string[i].isalpha() or string[i]==' '):
        p=string[letter:i]
        try:
            res+=p[0]*int(p[1:])
        except:
            res+=p[0]
        letter=i
    else:
        continue
if string[letter+1:] != str():
    res+=string[letter]*int(string[letter+1:])
else:
    res+=string[letter]
result =  open('text1.txt','w',encoding='UTF-8')
result.write(res)
result.close()

text = open('text.txt','r',encoding='UTF-8')
string=str()
for i in text:
    string+=i
res=''
letter=0
for i in range(1,len(string)):
    if(string[int(i)].isalpha() or string[int(i)]==' '):
        p=string[letter:i]
        res+=p[0]*int(p[1:])
        letter=i
    else:
        continue
res+=string[letter]*int(string[letter+1:]) 
result =  open('text1.txt','w',encoding='UTF-8')
result.write(res)
result.close()
print(res)

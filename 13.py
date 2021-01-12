a=input()
a.lower()
res=''
letter=0
for i in range(1,len(a)):
    if(a[i].isalpha() or a[i]==' '):
        p=a[letter:i]
        res+=p[0]*int(p[1:])
        letter=i
    else:
        continue
res+=a[letter]*int(a[letter+1:])
print(res)   
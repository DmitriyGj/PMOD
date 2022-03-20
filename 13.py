a=input()
a.lower()
res=''
letter=0
for i in range(1,len(a)):
    if(a[i].isalpha() or a[i]==' '):
        p=a[letter:i]
        try:
            res+=p[0]*int(p[1:])
        except:
            res+=p[0]
        letter=i
    else:
        continue
if a[letter+1:] != str():
    res+=a[letter]*int(a[letter+1:])
else:
    res+=a[letter]
print(res)   
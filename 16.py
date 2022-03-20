def kk(s):
    i =0
    count =len(s)
    while(i!=count):
        if s[i]>=0:
            s[i]%=3
        else:
            s.remove(s[i])
            count-=1
            continue
        i+=1
a=[int(i) for i in input().split()]
kk(a)
print(a)
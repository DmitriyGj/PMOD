a=input()
a.lower()
count = 1
res = a[0]
for i in a[1:]:
   if res[-1] == i: 
       count += 1
   else:
       if(count!=1):
           res += str(count) + i
       else:
           res+=i
       count = 1
if(count !=1 ):
    res += str(count)
print(res)
a=input()
a.lower()
count = 1
res = a[0]
for i in a[1:]:
   if res[-1] == i: 
       count += 1
   else:
       res += str(count) + i
       count = 1
res += str(count)
print(res)


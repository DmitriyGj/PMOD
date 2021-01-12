
a=[]
for i in input().split(): 
    if int(i) >=0:
        a.append(int(i)%3)
print(a)
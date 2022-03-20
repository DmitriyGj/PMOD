string =input().split()
for i in range(0,len(string)):
    if i != len(string)-1:
        print(string[i],end =' ')
    else:
        print(string[i])
    
        
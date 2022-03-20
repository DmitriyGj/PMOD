a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+2):
    if(i != a):
        print(i-1, end='\t')
    else:
        print(' ', end ='\t')
    for j in range(c,d+1):
        if(i == a):
            print(j,end='\t')
        else:
            print((i-1)*j, end='\t')
    print('\n')
        
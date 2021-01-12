import math

b =  [] 
a =''
i=1
check = False
a=input()
c=len(a.replace(' ',''))
while(a != 'end' ):
    if(i<=c and len(a.split())==c):
        i+=1
        b.append(a.split())
        a = input()
        check = True
    else:
        chek =False
        print('Матрица не квадратная ')
        break
if(check):
    p1 = float(0)
    for i in range(0,len(b)):
        for j in range(0,len(b)):
            p1+=float(b[i][j])*float(b[i][j])       
    print('p1 =',math.sqrt(p1))
    p2 = float()
    for i in range(0,len(b)):        
        mblarge = 0
        for j in range(0,len(b)):
            mblarge=abs(mblarge)+abs(float(b[j][i]))
        if(mblarge > p2):
            p2=mblarge
    print('p2 = ',p2)

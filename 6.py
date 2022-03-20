print("Введите число" )
a = float(input())
print("Введите отрезок ")
b = input().split(' ')
result =0
count =0
for i in range(int(b[0]),int(b[1])+1):
    if(i%a ==0 ):
        result +=i
        count+=1
if(result != 0):
    print(result/count)
else:
    print("Чисел кратных "+ a +"на отрезке ["+b[0]+","+b[1]+"]")
result = 0
count =0
c = int(b[0])
while(c != int(b[1])+1):
    if (c%a == 0 ):
        result+=c
        count+=1
    c+=1
if(result != 0):
    print(result/count)
else:
    print("Чисел кратных "+ a +"на отрезке ["+b[0]+","+b[1]+"]")
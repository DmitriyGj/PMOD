a = input().split()
x = input()
pos = 0 
for i in a:
    if(i==x):
        print(pos+1,end = ' ')
    pos+=1
if(pos == 0):
    print("Отсутствует")    
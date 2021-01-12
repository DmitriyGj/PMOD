d = dict().fromkeys(input('Введите ключи через пробел'+'\n').split())
for i in d:
    d[i] = input("Введите значения ключа "+i+'\n').split()
k=input('введите к ')
v=input('введите v ')
if k in d:
    d[k]+=v.split()
elif '-'+k in d:
    d['-'+k]+=v.split()
else:
    d[k]=v.split()      
print(d)
def Change(a):
    k=input('введите к ')
    v=input('введите v ')
    if k in d:
        a[k]+=v.split()
    elif '-'+k in d:
        a['-'+k]+=v.split()
    else:
        a['-'+k]=v.split() 
d = dict().fromkeys(input('Введите ключи через пробел'+'\n').split())
for i in d:
    d[i] = input("Введите значения ключа "+i+'\n').split()
Change(d)     
print(d)
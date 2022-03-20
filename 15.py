def  EvDist(a,b):
    result =0.0
    for i in range(0,len(a)):
        result+=(a[i]-b[i])**2
    result=result**(1/2)
    return result

n = input('Введите N = ')
a = list(int(i) for i in input("Введите вектор A \n").split())
print(len(a))
if(len(a) != int(n)):
    print('Error')
else:
    b=list(int(i) for i in input('Введите вектор B \n').split())
    if(len(b)!=len(a)):
        print('Error')
    else:
        print(EvDist(a, b))
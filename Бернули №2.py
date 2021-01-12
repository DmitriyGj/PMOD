import math as ma

def C(n,k):
    return ma.factorial(n)/(ma.factorial(n-k)*ma.factorial(k))
    
def bernuli(n,p,k):
    return(C(n,k)*ma.pow(p, k)*ma.pow(1-p, n-k))

def menee(n,p,m):
    result=0;
    for i in range(0,m):
        result+=C(n,i)*ma.pow(p, i)*ma.pow(1-p, n-i)
    return(result)
    
def ne_bolee(n,p,m):
    result=0;
    for i in range(0,m+1):
        result+=C(n,i)*ma.pow(p, i)*ma.pow(1-p, n-i)
    return(result)
    
def bolee(n,p,m):
    result=0;
    for i in range(m+1,n+1):
        result+=C(n,i)*ma.pow(p, i)*ma.pow(1-p, n-i)
    return(result)

def ne_menee(n,p,m):
    result=0;
    for i in range(m,n+1):
        result+=C(n,i)*ma.pow(p, i)*ma.pow(1-p, n-i)
    return(result)

bernuli(10,1/7,2)
menee(10,1/7,3)
ne_bolee(10,1/7,3)
bolee(10,1/7,8)
ne_menee(10,1/7,1)
print(ne_bolee(600,0.6,380)*ne_menee(600,0.6,340))

import scipy.stats as sts
import math as ma

def l_laplace (n,p,k):
    return sts.norm.pdf((k-n*p)/ma.sqrt(n*p*(1-p)))/ma.sqrt(n*p*(1-p))

def i_laplace(n, p, k_1, k_2):
    return (sts.norm.cdf((k_2-n*p)/ma.sqrt(n*p*(1-p)))-0.5)-(sts.norm.cdf((k_1-n*p)/ma.sqrt(n*p*(1-p)))-0.5)
                       
print(l_laplace(400,0.1,36))
print(l_laplace(400,0.1,50))
print(i_laplace(400,0.1,30,50))
print(i_laplace(400,0.1,36,400)-l_laplace(400,0.1,36))

n = 600
p= 0.6
q=1-p
print(i_laplace(n,p,340,380))
dx = n*p
e = 20
print(1-(n*p)/e**2)
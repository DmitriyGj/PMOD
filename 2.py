import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
import math as ma

plt.figure(figsize =(10,5))
x = np.linspace(0,20,1000)
lamda = 1/3
plt.subplot(1,2,1)    
expon_rv = sts.expon(scale=1/lamda)
cdf = expon_rv.cdf(x)
plt.plot(x, cdf)
    
plt.subplot(1,2,2)
pdf = expon_rv.pdf(x)
plt.plot(x, pdf)    

p = ma.exp(-5/3)-ma.exp(-75/30)
print("P(7.5<x<5) = "+str(p))

kva = ma.log(0.4)/-lamda
print("Квантиль = "+str(kva))

plt.figure(figsize=(10,5))

n=800
p=0.005

alpha=n*p
plt.subplot(1,2,1)
poisson_rv = sts.poisson(alpha)
x = np.linspace(0,25,26)
    
cdf = poisson_rv.cdf(x)
plt.plot(x, cdf)

plt.subplot(1,2,2)
pmf = poisson_rv.pmf(x)
plt.step(x, pmf,'o')

print("Матожидание = "+str(alpha))
print("Дисперсия = "+str(alpha))
print("Сигма = "+str(ma.sqrt(alpha)))
print("P(X=5) = "+str(poisson_rv.pmf(5)))
print("P(x=80) = "+str(poisson_rv.pmf(80)))
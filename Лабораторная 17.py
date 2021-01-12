import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
import math as ma

plt.figure(figsize = (10, 10) )
x = np.linspace(0,6,1000)

lamda =1.2
expon_rv = sts.expon(scale = 1 / lamda)
select = expon_rv.rvs(1000)
plt.hist(select, bins = 100, range=(0,5), density=True)
pdf = expon_rv.pdf(x)
plt.plot(x, pdf, label = "плотность показательного распределения c λ‎ = " + str(lamda))   

plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.title("Показательное распределение, lamda = 1.2")
plt.legend()

def GenerateSelection(n):
    generation = []
    for i in range(1000):
        generation.append(sum(expon_rv.rvs(n)) / n)
    return np.array(generation)
#2
selection5 = GenerateSelection(5)
selection10 = GenerateSelection(10)
selection20 = GenerateSelection(25)
selection100 = GenerateSelection(100)
selection500 = GenerateSelection(500)

#3
m5 = 1/lamda
m10 = 1/lamda
m25 = 1/lamda
m100 = 1/lamda
m500 = 1/lamda

sigma5 = m5/ma.sqrt(5)
sigma10 = m10/ma.sqrt(10)
sigma25 = m25/ma.sqrt(25)
sigma100 = m100/ma.sqrt(100)
sigma500 = m500/ma.sqrt(500)

#4
norm_rv5 = sts.norm(m5,sigma5)
norm_rv10 = sts.norm(m10,sigma10)
norm_rv25 = sts.norm(m25,sigma25)
norm_rv100 = sts.norm(m100,sigma100)
norm_rv500 = sts.norm(m500,sigma500)

plt.figure(figsize=(10,12))
plt.subplot(3,2,1)
plt.hist(selection5, bins = 100, range=(0,2), density=True, label='Выборка из 1000 значений СВ')
x=np.linspace(0,2,1000)
pdf = norm_rv5.pdf(x)
plt.plot(x,pdf)
plt.title("n = "+ str(5)+', σ = '+str(round(sigma5,3))+', m = '+str(round(m5,3)))

plt.subplot(3,2,2)
plt.hist(selection10, bins = 100, range=(0,2), density=True, label='Выборка из 1000 значений СВ')
x=np.linspace(0,2,1000)
pdf = norm_rv10.pdf(x)
plt.plot(x,pdf)
plt.title("n = "+ str(10)+', σ = '+str(round(sigma10,3))+', m = '+str(round(m10,3)))

plt.subplot(3,2,3)
plt.hist(selection20, bins = 100, range=(0,2), density=True, label='Выборка из 1000 значений СВ')
x=np.linspace(0,2,1000)
pdf = norm_rv25.pdf(x)
plt.plot(x,pdf)
plt.title("n = "+ str(25)+', σ = '+str(round(sigma25,3))+', m = '+str(round(m25,3)))

plt.subplot(3,2,4)
plt.hist(selection100, bins = 100, range=(0,2), density=True, label='Выборка из 1000 значений СВ')
x=np.linspace(0,2,1000)
pdf = norm_rv100.pdf(x)
plt.plot(x,pdf)
plt.title("n = "+ str(100)+', σ = '+str(round(sigma100,3))+', m = '+str(round(m100,3)))

plt.subplot(3,2,5)
plt.hist(selection500, bins = 100, range=(0,2), density=True, label='Выборка из 1000 значений СВ')
x=np.linspace(0,2,1000)
pdf = norm_rv500.pdf(x)
plt.plot(x,pdf)
plt.title("n = "+ str(500)+', σ = '+str(round(sigma500,3))+', m = '+str(round(m500,3)))

#5
# 1) Да
# 2) При увеличении n разница между среднее арифметическое n случайных элементов будет стремиться к мат ожиданию => сигма будет уменьшаться 
import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt
import math as ma

def emp_cdf(selection,x):
    selection = np.sort(selection) 
    return np.searchsorted(selection, x, side = 'right') / selection.size 


poisson_rv = sts.poisson(3)

smallSelection = poisson_rv.rvs(30)
largeSelection  = poisson_rv.rvs(200)

counterSelection = np.unique(smallSelection, return_counts = True)
x = counterSelection[0]
frequency = counterSelection[1]
rel_frequency = frequency/len(smallSelection)    

#Выборка n<=30
plt.figure(figsize=(25,15))
plt.subplot(2,3,1) 
plt.plot(x,frequency,'o-')
plt.title('Полигон частот')
plt.xlabel('Варинаты $x_i$')
plt.ylabel('Частоты $n_i$')

plt.subplot(2,3,2)
xt = np.linspace(0,15, 16)
pmf = poisson_rv.pmf(xt)
plt.plot(xt, pmf,'o-',label = 'Плотность пуассоновского распределение')
plt.plot(x,rel_frequency,'o-',label = 'Выборка')

plt.legend()
plt.title('Полигон относительных частот и многоугольник распределения')
plt.xlabel('Варинаты $x_i$')
plt.ylabel('Относительные частоты $w_i$')


plt.subplot(2,3,3)
cdf = poisson_rv.cdf(xt)
plt.step(xt,cdf,label ='Пуассоновское распределение' )
e_cdf=emp_cdf(smallSelection,xt)
plt.step(xt,e_cdf,label = 'Выборка')
plt.legend()
plt.title('Эмпирическая и "теоретическая" функции распределения')
plt.ylabel('$F^*(x)$ \ F(x)')
plt.xlabel('x')
print('1 выборка')
print('Среднее = ',round(np.mean(smallSelection)))
print('Медиана = ',np.median(smallSelection))
print('Мода = ', sts.mode(smallSelection)[0][0])
print('Исправленная выборочная дисперсия = ',np.var(smallSelection,ddof=1))
print('Исправленное среднее квадратическое отклонение = ',np.std(smallSelection,ddof=1))
print('Квантиль порядка 0.25 = ',np.quantile(smallSelection,0.7))
print('35-ый процентиль = ',np.percentile(smallSelection,35))


#выборка n>30
counterSelection = np.unique(largeSelection,return_counts = True)

x=counterSelection[0]
frequency = counterSelection[1]
rel_frequency=frequency/len(largeSelection)

plt.subplot(2,3,4) 
plt.plot(x,frequency,'o-')
plt.title('Полигон частот')
plt.xlabel('Варинаты $x_i$')
plt.ylabel('Частоты $n_i$')

plt.subplot(2,3,5) 
plt.plot(x,rel_frequency,'o-')

plt.plot(x,rel_frequency,'o-',label = 'Выборка')

xt = np.linspace(0, 20, 21)
pmf = poisson_rv.pmf(xt)

plt.plot(xt, pmf,'o-',label = 'Пуассоновское распределение')

plt.title('Полигон относительных частот и многоугольник распределения')
plt.xlabel('Варинаты $x_i$')
plt.ylabel('Относительные частоты $\omega_i$')
plt.legend()

plt.subplot(2,3,6)
cdf = poisson_rv.cdf(xt)
plt.step(xt,cdf,label ='Пуассоновское распределение' )
e_cdf=emp_cdf(largeSelection,xt)
plt.step(xt,e_cdf,label = 'Выборка')

plt.legend()
plt.title('Эмпирическая и "теоретическая" функции распределения')
plt.ylabel('$F^*(x)$ \ F(x)')
plt.xlabel('x')
plt.title('Эмпирическая и "теоретическая" функции распределения')
print('2 выборка')
print('Среднее = ',round(np.mean(largeSelection),0))
print('Медиана = ',np.median(largeSelection))
print('Мода = ', sts.mode(largeSelection)[0][0])
print('Выборочная дисперсия = ',np.var(largeSelection))
print('Выбррочное среднее квадратическое отклонение = ',np.std(largeSelection))
print('Квантиль порядка 0.25 = ',np.quantile(largeSelection,0.7))
print('35-ый процентиль = ',np.percentile(largeSelection,35))
# №3
plt.figure(figsize=(20,15))
lamda = 0.8
expon_rv = sts.expon(scale=1/lamda)

smallSelection=expon_rv.rvs(30)
largeSelection =expon_rv.rvs(200)

#n<=30
k=1+ma.floor(ma.log2(smallSelection.size))

plt.subplot(2,3,1)
histogram = np.histogram(smallSelection, bins = k)

hist_d = histogram[0]
bins_edges = histogram[1]
h = bins_edges[1] - bins_edges[0]
hist_dh = hist_d / h

plt.bar(bins_edges[:-1], hist_dh, align = 'edge', width = h)

plt.title('Гистограмма частот')
plt.ylabel('$n_i$')
plt.xlabel('$x_i$')

plt.subplot(2,3,2)
plt.title('Гистограмма относительных частот \n плотность пкоазательного распределения')
plt.hist(smallSelection, bins = k, density = True, label = 'Выборка')

xt=np.linspace(-1, max(smallSelection)+2, 200) 
pdf = expon_rv.pdf(xt)
plt.plot(xt, pdf, label = 'Показательное \nраспределение')

plt.ylabel('$\omega_i / h$ \ f(x)')
plt.xlabel('$x_i$ / x')
plt.legend()

plt.subplot(2,3,3)
e_cdf =emp_cdf(bins_edges, xt)
plt.plot(xt, e_cdf, label = 'выборка')
cdf = expon_rv.cdf(xt)
plt.plot(xt,cdf,label = "Показательное распределение")
plt.legend()
print('3 выборка')
print('Среднее = ',np.mean(smallSelection))
print('Медиана = ',np.median(smallSelection))
print('Мода = ', sts.mode(smallSelection)[0][0])
print('Исправленная выборочная дисперсия = ',np.var(smallSelection,ddof=1))
print('Исправленное среднее квадратическое отклонение = ',np.std(smallSelection,ddof=1))
print('Квантиль порядка 0.25 = ',np.quantile(smallSelection,0.7))
print('35-ый процентиль = ',np.percentile(smallSelection,35))
#n>30
k=1+ma.floor(ma.log2(largeSelection.size))

plt.subplot(2,3,4)
histogram = np.histogram(smallSelection, bins = k)

hist_d = histogram[0]
bins_edges = histogram[1]
h = bins_edges[1] - bins_edges[0]
hist_dh = hist_d / h

plt.bar(bins_edges[:-1], hist_dh, align = 'edge', width = h)

plt.title('Гистограмма частот')
plt.ylabel('$n_i$')
plt.xlabel('$x_i$')

plt.subplot(2,3,5)
plt.title('Гистограмма относительных частот \n плотность пкоазательного распределения')
plt.hist(largeSelection, bins = k, density = True, label = 'Выборка')

xt=np.linspace(-1, max(largeSelection)+2, 100) 
pdf = expon_rv.pdf(xt)
plt.plot(xt, pdf, label = 'Показательное \nраспределение')

plt.ylabel('$\omega_i / h$ \ f(x)')
plt.xlabel('$x_i$ / x')
plt.legend()

plt.subplot(2,3,6)
e_cdf =emp_cdf(bins_edges, xt)
plt.plot(xt, e_cdf, label = 'выборка')  
cdf = expon_rv.cdf(xt)
plt.plot(xt,cdf,label = "Показательное распределение")
plt.title('Эмпирическая и "теоретическая" функции распределения')
plt.ylabel('$F^*(x)$ \ F(x)')
plt.xlabel('x')
plt.legend()
print('4 выборка')
print('Среднее = ',np.mean(largeSelection))
print('Медиана = ',np.median(largeSelection))
print('Мода = ', sts.mode(largeSelection)[0][0])
print('Выборочная дисперсия = ',np.var(largeSelection))
print('Выбррочное среднее квадратическое отклонение = ',np.std(largeSelection))  
print('Квантиль порядка 0.25 = ',np.quantile(largeSelection,0.7))
print('35-ый процентиль = ',np.percentile(largeSelection,35))
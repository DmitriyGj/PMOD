import scipy.stats as sts
import numpy as np 

#                              №1

m=1
sigma=0.5
norm_rv = sts.norm(m,sigma)
#                              №2
n_s=20
n_l=90
smallSelection = norm_rv.rvs(n_s)
largeSelection = norm_rv.rvs(n_l)

#                              №3

middleOfSmall = np.mean(smallSelection)
middleOfLarge = np.mean(largeSelection)
print(f"Среднее выборочное для выборки n<=30 = {middleOfSmall}" )
print(f"Среднее выборочное для выборки n>30 = {middleOfLarge}")

deviationOfSmall = np.std(smallSelection,ddof=1)
print(f"Исправленное выборочное среднее квадратическое отклонение для выборки объема n<=30 = {deviationOfSmall}")


#                              №4
gamma = 0.95
intervalOfMiddleForSmallSelection = sts.t.interval(gamma, df= n_s-1, loc = middleOfSmall,scale = deviationOfSmall/n_s**0.5) 
print(f"Доверительный интервал среднего выборонНого для выборки n<=30 = {intervalOfMiddleForSmallSelection} (interval)")

t_rv=sts.t(df=n_s-1)
delta_small = t_rv.ppf((gamma+1)/2)*deviationOfSmall/n_s**0.5
inter_small = [middleOfSmall-delta_small,middleOfSmall+delta_small]
print(f"Доверительный интервал среднего выбороного для выборки n<=30 = {inter_small} (ppf)")

intervalOfMiddleForLargeSelection = sts.norm.interval(gamma, loc = middleOfLarge, scale = sigma/n_l**0.5)
print(f"Доверительный интервал среднего выбороного для выборки n>30 = {intervalOfMiddleForLargeSelection} (interval)")

delta_large = sts.norm.ppf((gamma+1)/2)*sigma/n_l**0.5
inter_large = [middleOfLarge-delta_large,middleOfLarge+delta_large]
print(f"Доверительный интервал среднего выбороного для выборки n>30 = {inter_large} (ppf)")
#                               №5

h1 = sts.chi2.ppf((1-gamma)/2,n_s-1)**0.5
h2 = sts.chi2.ppf((1+gamma)/2,n_s-1)**0.5
inter_s = [(deviationOfSmall*((n_s-1)**0.5))/h2,(deviationOfSmall*((n_s+1)**0.5))/h1]
print(f"Доверительный интервал для срденквадртаического отклонения =  {inter_s}")
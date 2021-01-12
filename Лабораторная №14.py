import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

def BuildOfUniform (a, b):

    uniform_rv = sts.uniform(a, b-a)
    x = np.linspace(0,5,1000)
    plt.subplot(2,2,1)
    cdf = uniform_rv.cdf(x)
    plt.step(x,cdf, label = 'a = '+str(a)+' b = '+str(b))
    
    plt.subplot(2,2,2)
    pdf = uniform_rv.pdf(x)
    plt.step(x,pdf, label = 'a = '+str(a)+', b = '+str(b))

# №1
m=1.0
sigma=0.2

norm_rv = sts.norm(m,sigma)
x = np.linspace(0,2,1000)

plt.figure(figsize=(16,16))
plt.subplot(2,2,1) 
cdf = norm_rv.cdf(x)
plt.plot(x, cdf)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
plt.title("Функция распределения нормального закона")

plt.subplot(2,2,2)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.title("Плотность вероятностей нормального закона")

#Проверка правлиа 3σ
plt.subplot(2,2,3)
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)
x = np.linspace(m,m,200)
y = np.linspace(0,norm_rv.pdf(x),200)
plt.plot(x,y,color = 'grey',linestyle = 'dashed')
plt.text(m-.02,-.17,'m',fontsize=8)
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.title("Проверка правила 3σ")
color = ['red','orange','green']
for i in [3.0,2.0,1.0] :
    pos_sigma = m+sigma*i
    rev_sigma = m-sigma*i
    cdf = norm_rv.cdf(pos_sigma) 
    x =np.linspace(pos_sigma,rev_sigma,200)
    y = np.linspace(cdf+i+.5,cdf+i+.5,200)
    plt.plot(x,y,color = color[int(i-1)])
    
    y = np.linspace(0,cdf+i+.5,200)

    x = np.linspace(pos_sigma,pos_sigma,200)
    plt.plot(x,y,color[int(i-1)],linestyle = 'dashed')    
    plt.text(pos_sigma-.015,cdf+i+.5,str(int(i))+'σ',fontsize=8)
    
    x = np.linspace(rev_sigma,rev_sigma,200)
    plt.plot(x,y,color[int(i-1)],linestyle = 'dashed')   
    plt.text(rev_sigma-.03,cdf+i+.5,str(-int(i))+'σ',fontsize=8)
    
    p = round(norm_rv.cdf(pos_sigma)-norm_rv.cdf(rev_sigma),4)
    plt.text(.95, cdf+i+.25, str(p))



# №2 
plt.figure(figsize = (12,6))

BuildOfUniform(1.5,3.5)
BuildOfUniform(2,3)
BuildOfUniform(1,4)

plt.subplot(2,2,1)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
plt.title("Функция распределения равномерного закона")
plt.legend()

plt.subplot(2,2,2)
plt.ylabel('$f(x)')
plt.xlabel('%x')
plt.title('Плотность распределения равномернного законна')
plt.legend()

# №3

plt.figure(figsize =(10,5))
x = np.linspace(0,8,1000)
for lamda in [0.1,0.5,1.0]:
    plt.subplot(1,2,1)     
    expon_rv = sts.expon(scale=1/lamda)
    cdf = expon_rv.cdf(x)
    plt.step(x, cdf,label = "λ = " + str(lamda))
    
    plt.subplot(1,2,2)
    pdf = expon_rv.pdf(x)
    plt.step(x, pdf,label = "λ = " + str(lamda))    
    
plt.subplot(1,2,1)    
expon_rv = sts.expon(scale=3)
cdf = expon_rv.cdf(x)
plt.step(x, cdf,label = "λ = " + str(3))
    


# №4
plt.figure(figsize=(10,5))
n=15
p=0.3

binomial_rv = sts.binom(n, p)

plt.subplot(1,2,1)
x = np.linspace(0,15,16)
cdf = binomial_rv.cdf(x)
plt.step(x,cdf)
plt.ylabel("F(x)")
plt.xlabel("x")
plt.title("Функция распределения биномиального закона")

plt.subplot(1,2,2)
pmf = binomial_rv.pmf(x)
plt.step(x,pmf,'o')
plt.ylabel("P(X = x)")
plt.xlabel('x')
plt.title("Вероятности биномиального закона")

# №5
plt.figure(figsize = (10,5))
for alpha in [1, 2, 3.5]:
    
    plt.subplot(1,2,1)
    poisson_rv = sts.poisson(alpha)
    x = np.linspace(0,12,13)
    
    cdf = poisson_rv.cdf(x)
    plt.step(x, cdf, label = "a = " + str(alpha))

    plt.subplot(1,2,2)
    pmf = poisson_rv.pmf(x)
    plt.step(x, pmf,"o", label = "a = " + str(alpha))
    
plt.subplot(1,2,1)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
plt.title("Функция распределения закона Пуассона")
plt.legend()
plt.subplot(1,2,2)
plt.ylabel('$P(X=x)$')
plt.xlabel('$x$')
plt.title("Вероятности закона Пуассона")
plt.legend()
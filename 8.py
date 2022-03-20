import math

result = 0
x = -1
i =0
res =1
while(abs(res) >= abs(10**(-5))):
    i+=1
    result+=res
    res=(x**i)/math.factorial(i)
print(result)
print(math.exp(x))
        
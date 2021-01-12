import numpy as np

a = np.array(list(int(i) for i in input('Введите вектор А ').split()))
b = np.array(list(int(i) for i in input('Введите ветор В ').split()))

s=np.linalg.norm(a-b)
print(s)
a = [int(i) for i in input().split()]
print(min(a))
print(max(a))
print([int(i) for i in a if i != min(a) and i!= max(a)][0])

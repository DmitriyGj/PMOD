a = int(input())
if (((a % 100) != 0 and (a % 4)==0) or(a % 400)==0 ):
    print("Високосный")
else: 
    print("Год не високосный")


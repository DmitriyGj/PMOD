print("Введите число a ")
a = float(input())
print("Введите число b ")
b = float(input())
print("Какую операцию выполнить ? 1 - сложить  2 - найти разность 3 - найти произведение 4 - поделить 5 - целочисленное деление 6 - нахождение остатка 7 - возведение в степень")
operation = int(input())
if(operation == 1):
    print(a+b)
elif(operation == 2):
    print(a-b)
elif(operation == 3):
    print(a*b)
elif(operation == 7):
    if(a ==0 and b <0):
        print("Невозможно выполнить операцию")
    else:
        print(a**b)
elif(operation == 4 or 5 or 6):
    if(b != 0):
        if(operation == 4):
            print(a/b)
        elif(operation==5):
            print(a//b)
        elif(operation == 6):
            print(a%b)
    else:
        print("Невозможно выполнить операцию")          
else:
    print("Такой операци нет")

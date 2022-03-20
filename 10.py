
a= input()
c=len(a.split())
matrix=[]
check = False
while a !='end':
    if len(a.split())==c:
        matrix.append(list(int(i) for i in a.split()))
        a=input()
        check=True
    else:
        check = False
        print('Матрица не прямоугольная')
        break
if(check):
    vector = []
    for i in matrix:
        vector.append(max(i))
    for i in vector:
        print(i, end = ' ')
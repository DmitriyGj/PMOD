spisok =dict()
for i in input().split():
    if i not in spisok:
        spisok[i]=1
    else:
        spisok[i]+=1
print(spisok)
string =input()
while string[len(string)-1]==' ':
    string=string[:-1]
while string[0]==' ':
    string=string[1:]
i=0
while i < len(string)-1:
    if string[i]==string[i+1]==' ':
        string = string[:i]+string[i+2:]
        i+=1
    else:
        i+=1
print(string)
    
        
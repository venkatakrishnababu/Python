L=['python 1991','c 1970','c++ 1985','java 1995','perl 1987']
for i in range(0,len(L)):
    for j in range(0,len(L)-1):
        if int(L[j].split()[1])>int(L[j+1].split()[1]):
            L[j],L[j+1]=L[j+1],L[j]
print(L)
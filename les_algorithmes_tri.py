list=[1,5,4,3,2,1]
def triselect(t):
    for i in range(len(t)):
        for j in range (i,len(t)):
            if t[j]>t[i]:
                aux=t[j]
                t[j]=t[i]
                t[i]=aux
def triabule(t):       
    for i in range(len(t)-1,0,-1):
        print(i)
        for j in range (0,i):
            if t.index(t[j]) != len(t)-1 :
                if t[j]<t[j+1]:
                    aux=t[j]
                    t[j]=t[i]
                    t[i]=aux
                
print(list)
triselect(t)
print(list)
        
import numpy as np
nl=int(input("nl"))
while nl<1 or nl>100 :
    nl=int(input("nl"))
nc=int(input("nc"))
while nc<1 or nc>100 :
    nc=int(input("nc"))    



l=int(input("l"))
while l<1 or l>nl :
    l=int(input("l"))
c=int(input("c"))
while c<1 or c>nc :
    c=int(input("nc")) 


n=int(input("n"))
while n<5 or n>12 :
    n=int(input("n"))     
s=np.array([str]*n)
for i in range(n):
    s[i]=input("entrer B ,H, D ou G")    
    while s[i] not in ["B","H","D","G"]:
        s[i]=input("entrer B ,H, D ou G")    
i=0            
while i<n and l<nl and c<nc and l>0 and c>0:
    if  s[i]=="D":
        c=c+1
    elif s[i]=="G":
        c=c-1
    elif s[i]=="B":
        l=l+1
    else:
        l=l-1
    i=i+1
if 0<=l<=nl and 0<=c<=nc :
    print("la position est :",l,c)    
else:
    print('hors grille')  

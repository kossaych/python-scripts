from math import*
e=input("donner l'equation de forme ax+bx+c")
e1=e[5]
plus="+"
moin="-"
pos1=e.find("x")
pos2=e.find("+")
pos3=e.find("x",pos1+1)
pos4=e.find("+",pos2+1)
a=e[0:pos1]
b=e[pos2:pos3]
c=e[pos3+1:]
a=float(a)
b=float(b)
c=float(c)
print(a)
print(b)
print(c)
print(e1)
delta=(b**2)-4*a*c
print(delta)
if e1==plus:
    
    if delta<0 :
            print("n'a pas des solition dans R")
    elif delta==0:
        print("s dans r =",-b/2*a)
    elif delta>0 :
        s1=-b+sqrt(delta)
        s2=-b-sqrt(delta)
        print("S dans R[",s1,"/",2*a,",",s2,"/",2*a,"]")
    else :
        print("equation invalide")
elif e1==moin :
     if delta<0 :
        print("n'a pas des solition dans R")
     elif delta==0:
        print("s dans r =",-b/2*a)
     elif delta>0 :
        s1=-b+sqrt(delta)
        s2=-b-sqrt(delta)
        print("S dans R[",s1,"/",2*a,",",s2,"/",2*a,"]")
    
else :
    print('invalide')
    


    






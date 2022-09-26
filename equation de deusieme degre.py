    from math import*
    e=input("donner l'equation de forme ax+bx+c")
    a=int(input("a :"))
    b=int(input("b :"))
    c=int(input("c :"))
    print("l'equation:"a,"x+",b,"x²+",c)
    delta=(b**2)-4*a*c
    print("delta :",delta)
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






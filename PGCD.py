print("le PGCD des nombre :")
N1=int(input("saisir le premier nombre :"))
N2=int(input("saisir le deusieme nombre :"))
if N1==0 or N2==0 :
    if N1==0:
         print("le PGCD : ",N2)
    else :
          print("le PGCD : ",N1)


elif  N2==N1 :
    print("le PGCD :",N1)    
elif N1 > N2 :
    Q=N1//N2
    R=N1%N2
    if R==0:   
            print("le PGCD : ",N2)
    else:
         while R != 0 :
               N1=N2
               N2=R
               Q=N1//N2
               C=R
               R=N1%N2
         print("le PGCD :",C)     
else :
     Q=N2//N1
     R=N2%N1
     if R==0:   
         print("le PGCD : ",N1)
     else:
         while R != 0 :
             N2=N1
             N1=R
             Q=N2//N1
             C=R
             R=N2%N1
         print("le PGCD :",C)  



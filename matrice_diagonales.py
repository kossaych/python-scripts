from numpy import array
n=4
M=array([[int]*n]*n)
v=1
for i in range(n):
    for j in range(n):
        M[i,j]=v
        v=v+1
ch=""    
for i in range(n*2-1):#(n*2-1-1,-1,-1):
    if i>n-1:
        for j in range(i-(n-1),n):#(n-1,i-(n-1)-1,-1):
            ch=ch+"*"+str(M[j,i-j])
    else:
        for j in range(i+1):#(i+1-1,-1,-1):
            ch=ch+"*"+str(M[j,i-j])
    print(ch)    
    ch=""

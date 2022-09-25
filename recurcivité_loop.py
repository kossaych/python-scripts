list=[]
def range(i,j):
    i=i
    if i==j:
        return i
    else : 
        list.append(i)
        return range(i+1,j)
range(0,10)
print(list)
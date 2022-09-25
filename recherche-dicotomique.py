liste=[1,2,3,4,5,6,10]
num=1

min = 0
max = len(liste)-1
midel = (min+max)//2
while min < max :
    if liste[midel] == num :
        break
    elif liste[midel] > num :
            max = midel-1
    else :
            min = midel+1
    midel= (min+max)//2
    
print(min)
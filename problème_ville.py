villes=[1,2,3,4,5,6,7,8,9,10]
class Distance:
  def __init__(self, v1, v2,v):
    self.v1= v1
    self.v2 = v2
    self.v=v
distances=[]    
for i in range(len(villes)):
    for j in range(len(villes)):
        if i==j :
            pass
        distances.append(Distance(i+1,j+1,i+j+7))


def proche(ville):
    min=1000
    for i in range(len(distances)):
        if distances[i].v1 == ville:
            if distances[i].v<min:
                min=distances[i].v
    return min
def cour(v_c):
    parcour=[]
    print(proche(1))
    for i in villes:
        parcour.append(proche(i))
        print(proche(i))
cour(5)
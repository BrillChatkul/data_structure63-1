class Sound:
    Wei = 0
    Ti = 0
    def __init__(self,Wei,Ti):
        self.Wei = Wei
        self.Ti = Ti
    def getWei(self):
        return self.Wei
    def getTi(self):
        return self.Ti
    def __str__(self):
        return str(self.Ti)



iNt = input('Enter Input : ').split(',')
Slist =[]
for i in iNt:
    So = i.split(' ')
    SoC = [int(x) for x in So]
    a = Sound(SoC[0],SoC[1])
    Slist.append(a)


z = 0
while z < len(Slist):
    j = z
    while j > -1:
        if Slist[z].Wei > Slist[j].Wei:
            print(Slist[j].Ti)
            Slist.pop(j)
            z -= 1
        j-=1
    z += 1

#print(Slist[0])



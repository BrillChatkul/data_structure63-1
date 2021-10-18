class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if self.items != None:
            i = self.items[0]
            self.items.pop(0)
            return i
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def showS(self):
        H = ''
        for x in range(len(self.items)):
            H += self.items[x]
            if x != len(self.items)-1:
                H += ', '
        return H

def checkG(lol):
    if lol == '0':
        return 'Eat'
    elif lol == '1':
        return 'Game'
    elif lol == '2':
        return 'Learn'
    elif lol == '3':
        return 'Movie'

def checkP(lol):
    if lol == '0':
        return 'Res.'
    elif lol == '1':
        return 'ClassR.'
    elif lol == '2':
        return 'SuperM.'
    elif lol == '3':
        return 'Home'


it = input('Enter Input : ').split(',')
MY = Queue()
YO = Queue()
for x in it:
    z = x.split(' ')
    MY.enQueue(z[0])
    YO.enQueue(z[1])

print('My   Queue =',MY.showS())
print('Your Queue =',YO.showS())
score = 0
MYI = Queue()
YOI = Queue()
while MY.size() > 0:
    MYLs = MY.deQueue().split(':')
    YOLs = YO.deQueue().split(':')
    if MYLs[0] == YOLs[0] and MYLs[1] != YOLs[1]:
        score += 1
    elif MYLs[0] != YOLs[0] and MYLs[1] == YOLs[1]:
        score += 2
    elif MYLs[0] == YOLs[0] and MYLs[1] == YOLs[1]:
        score += 4
    elif MYLs[0] != YOLs[0] and MYLs[1] != YOLs[1]:
        score -= 5
    M = checkG(MYLs[0])+':'+checkP(MYLs[1])
    MYI.enQueue(M)
    Y = checkG(YOLs[0])+':'+checkP(YOLs[1])
    YOI.enQueue(Y)
print('My   Activity:Location =',MYI.showS())
print('Your Activity:Location =',YOI.showS())
if score >= 7:
    print('Yes! You\'re my love! : Score is ',score,'.',sep='')
elif score > 0:
    print('Umm.. It\'s complicated relationship! : Score is ',score,'.',sep='')
else:
    print('No! We\'re just friends. : Score is ',score,'.',sep='')
    
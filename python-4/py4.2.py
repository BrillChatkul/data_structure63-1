class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        print(self.items[0])
        self.items.pop(0)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
iT = input('Enter Input : ').split(',')
EN = Queue()
ES = Queue()
for i in iT:
    i = i.split(' ')
    if i[0] == 'EN':
        EN.enQueue(i[1])
    elif i[0] == 'ES':
        ES.enQueue(i[1])
    elif i[0] == 'D':
        if ES.isEmpty() != True:
            ES.deQueue()
        elif ES.isEmpty() == True and EN.isEmpty() != True:
            EN.deQueue()
        elif ES.isEmpty() == True and EN.isEmpty() == True:
            print('Empty')
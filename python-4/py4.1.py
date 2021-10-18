class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def enQueue(self,i):
        self.items.append(i)
        print('Add',i,'index is',len(self.items)-1)
    def deQueue(self):
        print('Pop',self.items[0],end=' ')
        self.items.pop(0)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
        
        
iT = input('Enter Input : ').split(',')
TQue = Queue()
for i in iT:
    i = i.split(' ')
    if i[0] == 'E':
        TQue.enQueue(i[1])
    elif i[0] == 'D':
        # print(bool(TQue.isEmpty)
        if TQue.isEmpty() == False:
            TQue.deQueue()
            print('size in queue is',TQue.size())
        else:
            print('-1')
if TQue.isEmpty() == False:
    print('Number in Queue is : ',TQue.items)
else:
    print('Empty')
# E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D

    
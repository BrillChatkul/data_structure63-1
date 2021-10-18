class Queue:
    def __init__(self,inPut):
        self.items = []
        if inPut != None:
            for j in inPut:
                self.items.append(j)
    
    def size(self):
        return len(self.items)
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            Im = self.items[0]
            self.items.pop(0)
            return Im
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

def encodemsg(Que11,Que2):
    Encode = Queue(None)
    C = Que2
    Que1 = Queue(x for x in Que11.items)
    while Que1.isEmpty()!=True:
        m = Que1.deQueue()
        if(m != ' '):
            b = int(C.deQueue())
            C.enQueue(b)
            x = ord(m) + b
            if x>122 or (x > 90 and x < 97):
                x -= 26
            Encode.enQueue(chr(x))
            
    print('Encode message is : ',Encode.items)

def decodemsg(Qq1,Qq2):
    Decode = Queue(None)
    while Qq1.isEmpty()!=True:
        m = Qq1.deQueue()
        if(m != ' '):
            Decode.enQueue(m)
            
    print('Decode message is : ',Decode.items)

It = input('Enter String and Code : ').split(',')
q1 = Queue(It[0])
q2 = Queue(It[1])
encodemsg(q1, q2)
decodemsg(q1, q2)
    
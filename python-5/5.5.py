class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.preview = None
class SortLinkList:
    def __init__(self):
        self.head = None
    
    
    def __str__(self):
        if not self.isEmpty():
            P = self.head
            S = str(self.head.data)
            while P.next is not None:
                P = P.next
                S += " "+str(P.data)
            return S
        else:
            return ''

    def add(self,item):
        Node_item = Node(item)
        if self.isEmpty():
            self.head = Node_item
        else:
            MainNode = self.head
            while MainNode.next is not None:
                MainNode = MainNode.next
            MainNode.next = Node_item
            Node_item.preview = MainNode
    def isEmpty(self):
        return self.head == None
    def addFront(self,item):
        Node_item = Node(item)
        if self.isEmpty():
            self.head = Node_item
        else:
            main_Node = self.head
            self.head = Node_item
            Node_item.next = main_Node
            main_Node.preview = Node_item

    def Indexof(self,I):
        if self.head != None:
            index = 0
            main_Node = self.head
            NotFound = False
            while index < I:
                if main_Node.next is not None:
                    main_Node = main_Node.next
                    index += 1
                else:
                    NotFound = True
                    break
            if NotFound == False:
                return main_Node
            else:
                return None

        else:
            return None

    def deQueue(self):
        Head_Node = self.head
        if Head_Node.next is not None:
            New_HeadNode = Head_Node.next
            self.head = New_HeadNode
            New_HeadNode.preview = None
        else:
            self.head = None
        Head_Node.next = None
        return Head_Node
    
    def SortList(self):
        if not self.isEmpty():
            Main_Node = self.head
            Slist = []
            while Main_Node is not None:
                Slist.append(Main_Node.data)
                Main_Node = Main_Node.next
            Slist.sort()
            self.head = None
            for i in Slist:
                self.add(i)
    
                 


def radix_sort(l):
    q = SortLinkList()
    for count in l:
        num = int(count)
        q.add(num)
    max_bits = get_max_bits(max(l))
    qq = SortLinkList()
    for A in range(10):
        qq.add(SortLinkList())
    
    CheckBreak = False
    times = -1
    for i in range(1,max_bits+2):
        while not q.isEmpty():
            num = q.deQueue()
            num_digit = get_digit(abs(num.data),i)
            qq.Indexof(num_digit).data.add(num.data)
        print('------------------------------------------------------------')
        print('Round : {0}'.format(i))
        if qq.Indexof(1).data.isEmpty() and qq.Indexof(2).data.isEmpty() and qq.Indexof(3).data.isEmpty() and qq.Indexof(4).data.isEmpty() and qq.Indexof(5).data.isEmpty() and qq.Indexof(6).data.isEmpty() and qq.Indexof(7).data.isEmpty() and qq.Indexof(8).data.isEmpty() and qq.Indexof(9).data.isEmpty():
            CheckBreak = True
        for i in range(10):
            qq.Indexof(i).data.SortList()
            print('{0} : {1}'.format(i,qq.Indexof(i).data))
            while not qq.Indexof(i).data.isEmpty():
                q.add(qq.Indexof(i).data.deQueue().data)
        times += 1
        if CheckBreak == True:
            break
      
    print('------------------------------------------------------------\n{0} Time(s)\nBefore Radix Sort : {1}'.format(times,l[0]),end='')
    for i in range(1,len(l)):
        print(' -> {0}'.format(l[i]),end='')
    print('')
    S = 'After  Radix Sort : '+str(q.deQueue().data)
    while not q.isEmpty():
        S += " -> "+str(q.deQueue().data)
    print(S)

def get_digit(n,d):
    for i in range(d-1):
        n//=10
    return n % 10

def get_max_bits(n):
    z = int(n)
    i = 0
    while z > 0:
        z //= 10
        i += 1
    return i

I = input("Enter Input : ").split(' ')
Input_number = [int(x) for x in I]
radix_sort(Input_number)


    





    
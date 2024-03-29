class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        if self.isEmpty(): return "linked list : "
        return "linked list : "+"->".join(str(i) for i in self.display())

    def reverse(self):
        if self.isEmpty(): return "reverse : "
        return "reverse : "+"->".join(str(i) for i in reversed(self.display()))

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node

    def isEmpty(self):
        return self.head.next == None

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        return elems
    
    def insert(self,index,data):
        if index > self.lenght() or index < 0:
            #print ("Data cannot be added")
            return None
        elif index == 0:
            self.appendHead(data)
            return self.display()
        elif index == self.lenght():
            self.append(data)
            return self.display()
        cur_idx = 1
        cur_node = self.head
        new_node = node(data)
        while True:
            cur_node = cur_node.next
            if cur_idx == index : 
                new_node.next = cur_node.next
                cur_node.next = new_node
                return new_node.data
            cur_idx += 1
    
    def appendHead(self,data):
        new_node = node(data)
        new_node.next = self.head.next
        new_head = node()
        new_head.next = new_node
        new_node.prev = new_head
        self.head = new_head

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def remove(self,data):
        cur = self.head
        inx = 0
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if cur.data == data:
                last_node.next = cur.next if cur.next != None else None
                return inx
            inx += 1

def main():
    Input = input('Enter Input : ').split(',')
    Linked_list = doublyLinkedList()

    for i in Input:
        i = i.strip().split()
        if i[0] == 'Ab':
            Linked_list.appendHead(int(i[1]))
        elif i[0] == 'A':
            Linked_list.append(int(i[1]))
        elif i[0] == 'I':
            ins = i[1].split(':')
            if  Linked_list.insert(int(ins[0]),int(ins[1])) != None:
                print('index = {} and data = {}'.format(int(ins[0]),int(ins[1])))
            else:
                print ("Data cannot be added")            
        elif i[0] == 'R':
            data = Linked_list.remove(int(i[1]))
            print('removed : {} from index : {}'.format(i[1],data) if data != None else 'Not Found!')
        print(Linked_list)
        print(Linked_list.reverse())
            
if __name__=='__main__':
    main()

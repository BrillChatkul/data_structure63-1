Input = input('Enter Input : ').split(',')
Count = []
for x in Input:
    if x != 'B':
        Tree = x.split(' ')
        Tree[1] = float(Tree[1])
        if len(Count) != 0:
            for z in range(len(Count)-1,-1,-1):
                if Tree[1] >= Count[z][1]:
                    Count.pop()
                else:
                    break
            Count.append(Tree)
        
            
        else:
            Count.append(Tree)
    
    if x == 'B':
        print(len(Count))
               
        
#A 9,A 4,A 6,B,A 5,A 8,B,A 5,A 2,B,A 10,B
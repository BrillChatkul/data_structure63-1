Input = input('Enter Input : ').split(',')
Count = []
Ipt = []
CountS = []
CC = []
Poison = 0
for x in Input:
    if x != 'B' and x != 'S':
        
        Tree = x.split(' ')
        Tree[1] = float(Tree[1])
        CC.append(Tree)
        
 
    elif x == 'S':
        Poison += 1

    elif x == 'B':
        CountS = CC.copy()
        # CountS = [xx for xx in CC]   #A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
        for zz in range(len(CountS)):
            if CountS[zz][1] % 2 == 0:
                CountS[zz][1] -= 1*Poison
                if CountS[zz][1] < 1:
                    CountS[zz][1] = 1
            elif CountS[zz][1] % 2 == 1:
                CountS[zz][1] += 2*Poison   
        print(CountS)
        print('CC',CC)
        
        if len(CountS) != 0:
            F = len(CountS)-1
            while F > 0:
                K = F-1
                while K >= 0:
                    if CountS[F][1] >= CountS[K][1]:
                        # print('Remove',CountS[K][1])
                        CountS.pop(K)
                        F -= 1
                    K -= 1
                F -= 1
        
         
        print(len(CountS))
        Poison = 0
    
               
        
#A 9,A 4,A 6,B,A 5,A 8,B,A 5,A 2,B,A 10,B
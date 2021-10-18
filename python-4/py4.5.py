iT = input('Enter Input (Normal, Mirror) : ').split(' ')
Mir = []
EQ = []
ECount = 0

Nor = []
NCount = 0
ER = 0

for i in iT[1]:
    if len(Mir)<2:
        Mir.append(i)
    elif len(Mir)>=2:
        if Mir[-1] == i and Mir[-2] == i:
            EQ.append(i)
            Mir.pop()
            Mir.pop()
            ECount += 1
        else:
            Mir.append(i)

for i in iT[0]:
    if len(Nor)<2:
        Nor.append(i)
    elif len(Nor)>=2:
        if Nor[-1] == i and Nor[-2] == i:
            if len(EQ) != 0:
                if len(Nor)>=2 and Nor[-1] == EQ[-1] and Nor[-2] == EQ[-1]:
                    Nor.pop()
                    Nor.pop()
                    ER += 1
                else:
                    Nor.append(EQ[-1])
                EQ.pop(-1)

                if len(Nor)>=2 and Nor[-1] == i and Nor[-2] == i:
                    Nor.pop()
                    Nor.pop()
                    NCount += 1
                else:
                    Nor.append(i)
                    

                
            else:
                Nor.pop()
                Nor.pop()
                NCount += 1
        else:
            Nor.append(i)
sNor = ''
if len(Nor)>0:
    for i in Nor:
        sNor += i
else:
    sNor += 'ytpmE'
print('NORMAL :',len(Nor),sNor[::-1],sep='\n')
print(NCount,'Explosive(s) ! ! ! (NORMAL)')
if ER > 0:
    print('Failed Interrupted',ER,'Bomb(s)')
print('------------MIRROR------------')
sMir = ''
if len(Mir)>0:
    for i in Mir:
        sMir += i
else:
    sMir += 'ytpmE'
print(': RORRIM',len(Mir),sMir,sep='\n')
print('(RORRIM) ! ! ! (s)evisolpxE',ECount)

        
        
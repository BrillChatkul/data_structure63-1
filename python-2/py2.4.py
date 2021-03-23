def Array_Sum(listQ):
    data = listQ.split()
    liss = []
    if len(data) > 2:
        for x in range(len(data)):
            for y in range(len(data)):
                if y != x:
                    for z in range(len(data)):
                        if z != y and z != x:
                            if int(data[x]) + int(data[y]) + int(data[z]) == 0:
                                lis = []
                                lis.append(int(data[x]))
                                lis.append(int(data[y]))
                                lis.append(int(data[z]))
                                if len(liss) == 0:
                                    liss.append(lis)
                                trueab = 0
                                for i in liss:
                                    if sorted(i) == sorted(lis):
                                        trueab = 1
                                if trueab == 0:
                                    liss.append(lis)
        return liss
    elif len(data) < 3:
        return 'Array Input Length Must More Than 2'

Qint = input('Enter Your List : ')
print(Array_Sum(Qint))
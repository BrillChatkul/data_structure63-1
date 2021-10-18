DataInput = input('Enter Input : ').split()
DataSort = []
Combo = 0
for x in DataInput:

    DataSort.append(x.upper())
    if(len(DataSort)>2):
        if x == DataSort[len(DataSort)-2] and x == DataSort[len(DataSort)-3]:
            DataSort.pop()
            DataSort.pop()
            DataSort.pop()
            Combo += 1
print(len(DataSort))
if len(DataSort)!=0:
    for y in range(len(DataSort)-1,-1,-1):
        print(DataSort[y],end='')
    print()
else:
    print('Empty')
if Combo > 1:
    print('Combo :',Combo,'! ! !')



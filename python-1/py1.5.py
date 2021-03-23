num = int(input('Enter Input : '))
y = 0
while y < num+1:
    i = 0
    while i < 1+num-y:
        print('.',end='')
        i+=1
    
    j = 0
    while j < 1+y:
        print('#',end='')
        j+=1
    if y == 0:
        plus = 0
        while plus < 2+num:
            print('+',end='')
            plus+=1
    else:
        print('+',end='')
        plus = 0
        while plus < num:
            print('#',end='')
            plus+=1
        print('+',end='')
    print()
    y += 1
ExY = 0
while ExY < 2:
    z = 0
    while z < 2+num:
        print('#',end='')
        z+=1
    xz = 0
    while xz < 2+num:
        print('+',end='')
        xz+=1
    print()
    ExY+=1

y1 = 0
while y1 < 1+num:
    if y1 == num:
        plus = 0
        while plus < 2+num:
            print('#',end='')
            plus+=1
    else:
        print('#',end='')
        plus = 0
        while plus < num:
            print('+',end='')
            plus+=1
        print('#',end='')
    i = 0
    while i < 1+num-y1:
        print('+',end='')
        i+=1
    
    j = 0
    while j < 1+y1:
        print('.',end='')
        j+=1
    print()
    y1 += 1

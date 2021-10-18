_st = input('Enter Input : ')
u=0
i=0
p=0
q=0

for z in _st:      
    if z == '(':
        u += 1
    elif z == ')':
        i += 1
    elif z == '[':
        p += 1
    elif z == ']':
        q += 1

rl = abs(u-i)+abs(p-q)
print(rl)
if rl == 0:
    print('Perfect ! ! !')
def mapping(ChangeString):
    int_list = []
    Character_list = []
    for x in range(len(ChangeString)):
        if x != 0:
            Have = 0
            for z in range(x):
                if ChangeString[x] == ChangeString[z]:
                    Have = 1
                    break
            if(Have == 0):
                Character_list.append(ChangeString[x])
        elif x == 0:
            Character_list.append(ChangeString[0])
    
    for x in range(len(ChangeString)):
        for y in range(len(Character_list)):
            if Character_list[y] == ChangeString[x]:
                int_list.append(y)

    
    return int_list

input_String = input('Enter String : ')
print(mapping(input_String))
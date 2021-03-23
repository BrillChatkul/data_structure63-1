
def num_grid(lst):

    for y in range(len(lst)):
      for x in range(len(lst[y])):
        if lst[y][x] == '-':
          lst[y][x] = 0
        elif lst[y][x] == '#':
          lst[y][x] = 10
    
    for y in range(len(lst)):
      for x in range(len(lst[y])):
        if lst[y][x] >= 10:
          if y-1>=0:
            if x-1>=0:
              lst[y-1][x-1] += 1
            lst[y-1][x] += 1
            if(x+1)<=len(lst[y])-1:
              lst[y-1][x+1] += 1
          if x-1>=0:
            lst[y][x-1] += 1
          if(x+1)<=len(lst[y])-1:
            lst[y][x+1] += 1
          if y+1<=len(lst)-1:
            if x-1>=0:
              lst[y+1][x-1] += 1
            lst[y+1][x] += 1
            if x+1<=len(lst[y])-1:
              lst[y+1][x+1] += 1
    
    for y in range(len(lst)):
      for x in range(len(lst[y])):
        if lst[y][x] >= 10:
          lst[y][x] = '#'
        lst[y][x] = str(lst[y][x])

    
      
    #Code Here

    return lst





lst_input = []
print('*** Minesweeper ***')
input_list = input('Enter input(5x5) : ').split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")
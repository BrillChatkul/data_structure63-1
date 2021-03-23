print('*** Fun with permute ***')
data = input('input : ')
data_list = data.split(',')
int_list = [int(x) for x in data_list]
print('Original Cofllection: ',int_list)
print('Collection of distinct numbers:')
result_perms = [[]]
for n in int_list:
    new_perms = []
    for perm in result_perms:
        for i in range(len(perm)+1):
            new_perms.append(perm[:i]+[n]+perm[i:])
            result_perms = new_perms
print('',result_perms)


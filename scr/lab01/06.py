n = int(input('in_1: '))
count_true = count_false = 0
for i in range(n):
    if input(f'in_{i+2}: ').split()[-1]=='True':
        count_true+=1
    else:
        count_false+=1
print(f'out: {count_true} {count_false}')
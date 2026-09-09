n = int(input())
count_true = count_false = 0
for n in range(n):
    if input().split()[-1]=='True':
        count_true+=1
    else:
        count_false+=1
print(count_true,count_false)
line = input()
first_index=second_index=-1
for i in line:
    if i.isupper() and first_index==-1:
        first_index=line.index(i)
    if i.isdigit() and second_index==-1:

        second_index=line.index(i)+1
word=''
for i in range(first_index,len(line),second_index-first_index):
    word+=line[i]
print(word)

file = open("text.txt",'r')
f = file.readlines()
newList = []
for line in f:
    if line[-1] =='\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
print(newList)
file.close()

file = open('file.txt','w')
file.write('Hello\n')
file.close()

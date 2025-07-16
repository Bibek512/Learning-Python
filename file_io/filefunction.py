f=open('file.txt')
# l=f.readlines()
# print(l)

for l in f:
    if l!='\n':
        print(l,end='')
f.close()
with open('replace.txt') as r:
    word=r.read()

with open('replace.txt','w') as r:
    r.write(word.replace('biatch', "buddy"))

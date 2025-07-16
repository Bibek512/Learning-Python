with open('poem.txt') as p:
    s=p.read()
    
    if 'buffalo' in s:
        print('Yes the word buffalo is there')

    else:
        print('No the word buffalo is not there')
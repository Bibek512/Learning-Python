
def table(n):
    with open(f"table/table of{n}.txt",'w')as t:
     
        t.write(f'TABLES OF {n}\n')
        for i in range(1,11):
           t.write(str(f'{n}*{i}={n*i}\n'))

print('\n')


for n in range(2,21):
    table(n)
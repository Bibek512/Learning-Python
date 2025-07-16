l=[1,5,20,10]
final=lambda x: x*x
sqlist=map(final,l)
print(list(sqlist))

def even(n):
    if(n%2==0):
        return True
    
evennbr=filter(even,l)
print(list(evennbr))

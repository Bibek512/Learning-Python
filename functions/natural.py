n= int(input(' enter the numbers :'))

def sum(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+sum(n-1)
    
a=print(f'the sum of natural number up to {n} is {sum(n)}')
import random
number=random.randint(1,100)
guessnbr=int(input("Enter your guess: "))
count=1

while(guessnbr!=number):

    if(guessnbr>number):
        print("Lower Number Please ")
        count+=1
    elif(guessnbr<number):
        print("Higher Number Please ")
        count+=1
    
    guessnbr=int (input(("Try Agian: ")))

print(f"The number was {number} and you guessed it in attempt {count}")
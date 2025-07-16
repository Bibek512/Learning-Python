import random
def game():
    score=random.randint(1,100)
    print(f'your score is {score}')
    with open("highscore.txt") as h:
       highscore= h.read()
       if(highscore!=''):
           highscore=int(highscore)
       else:
           highscore=0

    if(score>highscore):
        with open("highscore.txt",'w') as s:
            s.write(str(score))


game()

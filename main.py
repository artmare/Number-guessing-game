import random

num1 = 0 
num2 = 0 
usernum = 0
guessnum = 0
chances = 10

num1 = int(input('Write a first num --> '))
num2 = int(input('Write a second num --> '))

guessnum = random.randint(num1, num2)

usernum = int(input('Guess a num --> '))
    

while True:
    
    if usernum == guessnum:
        print("It is correct!")
        break
    
    elif abs(guessnum - usernum) > (usernum+guessnum)/2 and chances != 0:
        print("Not right but it is smaller")
        chances -= 1
        usernum = int(input('Guess a num --> '))
        
    elif abs(guessnum - usernum) < (usernum+guessnum)/2 and chances != 0:
        print("Not right but it is bigger")
        chances -= 1
        usernum = int(input('Guess a num --> '))
        
    elif abs(guessnum - usernum) == (usernum+guessnum)/2 and chances != 0:
        print("Not right but it is close")
        chances -= 1
        usernum = int(input('Guess a num --> '))
        
    else:
        print('try again')
        break

    
    
    
        
    
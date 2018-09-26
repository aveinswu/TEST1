#20180926 if else
import random

print('-------Hello World Python------')
temp=input('please input a number :')
guess = int(temp)

if guess ==random.randint(0,10) :
    print ('U ARE BINGO!')
else:
    print(' U MISS IT')

print('exit the game')
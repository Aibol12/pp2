import random
print("Hello! What is your name?")
name=str(input())
number=random.randint(1,21)
print("Well, "+name+" I am thinking of a number between 1 and 20")
g=0
countg=0
while(g!=number):
    print("take a guess")
    g=int(input())
    if(g<number):
        print("your guess is too low")
    else:
        print("your guess is too high")
    countg+=1
print("Good job, "+name+", You guessed my number in "+str(countg)+" guesses!")
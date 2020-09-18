import random

random_number= random.randint(1,101)
print(random_number)
c=0
guess=-99

while(guess != random_number):

    guess = int(input("Enter your guessed int number: "))

    if(guess>random_number):
        print("Higher")
    elif(guess<random_number):
        print("Lower")
    else:
        print("You guessed it right!!!")
    c=c+1

print("You have taken",str(c),"steps to guess the number")
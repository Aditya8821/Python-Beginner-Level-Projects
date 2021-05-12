import random
print("\t\t\t    --:Guessing Game:--")
print("Guess number between 1 and 10")
num=random.randint(1,10)
chance=0
print("You have 3 chance")
while chance<3:
    guess=int(input("Enter the guessed number:- "))
    if num>guess:
        print("You LOSE: Entered number is too smaller")
    elif num==guess:
        print("You WON")
        break
    elif num<guess:
        print("You LOSE: Entered number is too larger")
    chance+=1
if chance>2:
    print("You LOSE..Number is",num)

   

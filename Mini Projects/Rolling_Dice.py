import random
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    print("Rolling Dices......")
    print("The Values are.....")
    print("=>",random.randint(1,6))
    print("=>",random.randint(1,6))
    roll_again=input("Want to roll the Dices again? ") 

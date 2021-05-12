from random import randint
t=["Rock","Paper","Scissor"]
comp=t[randint(0,2)]
c="Yes"
while c=="Yes":
    player=input("Rock,Paper or Scissor? ")
    if player==comp:
        print("Tie!")
    elif player=="Rock":
        if comp=="Paper":
            print("You Lose!",comp,"smashed",player)
        else:
            print("You WON!",player,"smashed",comp)
    elif player=="Paper":
        if comp=="Scissor":
            print("You Lose!",comp,"smashed",player)
        else:
            print("You WON!",player,"smashed",comp)
    elif player=="Scissor":
        if comp=="Rock":
            print("You Lose!",comp,"smashed",player)
        else:
            print("You WON!",player,"smashed",comp)
    else:
        print("That's not a valid Word")
    choise=input("Press y to Play Again ")
    if choise=="y":
        c="Yes"
    else:
        c="No"
    

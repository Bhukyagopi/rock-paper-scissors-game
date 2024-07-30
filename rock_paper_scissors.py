import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
while True:
    choice=int(input("enter your choice"))
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    while choice>3 or choice<1:
        print("enter a valid choice!")

    if choice==1:
        choice_name="rock"
    elif choice==2:
        choice_name="paper"
    else:
        choice_name="scissors"
    
    print("your choice is ",choice_name)
    print("Now its computer's choice:")

    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name="rock"
    elif comp_choice==2:
        comp_choice_name="paper"
    else:
        comp_choice_name="scissors"
    
    print("computer choice is ",comp_choice_name)

    if(choice==comp_choice):
        print("Its draw!")
        result="draw"

    if(choice==1 and comp_choice==2):
        result="paper"
    elif(choice==1 and comp_choice==3):
        result="rock"
    elif(choice==2 and comp_choice==1):
        result="paper"
    elif(choice==2 and comp_choice==3):
        result="scissors"
    elif(choice==3 and comp_choice==1):
        result="rock"
    elif(choice==3 and comp_choice==2):
        result="scissors"
    
    if result=="draw":
        print("its tie!")
    elif result==choice_name:
        print("you won!")
    else:
        print("computer wins")

    print("do u want to play again(Y/N):")
    ans=input().lower()
    if ans=='n':
        break
print("thanks for playing")
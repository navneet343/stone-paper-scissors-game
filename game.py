import random
print("--- welcome to stone ,paper, scissors game ! ---")
choices = [ "stone" ,"paper" ,"scissors"]

user_score = 0
computer_score = 0

while True:
    user_choice = (
        input("enter your (stone, paper,scissors or ' quit' to exit :")
        .lower()
        .strip()
    )
    if user_choice == "quit":
        print("\n---final score---")
        print(f"you :{ user_score} | computer : {computer_score}")
        if user_score > computer_score :
           print("congratulations ! you won the match ")
        elif user_score < computer_score:
           print("computer won the match ! better luck next time ")
        else:
           print("it's a draw overall!")
        print (" thanks for playing !")
        break
    if user_choice not in choices :
        print(" invalid choice ! try again .")
        continue

    computer_choice = random.choice(choices)
    print( f"computer choice : {computer_choice}")

    if user_choice == computer_choice:
      print(" it's a tie")
    elif (
        (user_choice == "stone" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "stone" ) or
        (user_choice == "scissors" and computer_choice == "paper")
   ):
      print(" you win")
      user_score += 1

    else:
     print("computer wins ")
     computer_score +=1



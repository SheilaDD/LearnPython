import random

Play = input("Lets Play \n")

print("Winning rules are:\n"
      + "Rock vs Paper wins \n"
      + "Rock vs Scissors wins \n"
      + "Paper vs Scissors wins \n")

while True:
    print("Enter you choice: 1-Rock , 2-Paper, 3-Scissors")
    choice = int(input("Enter your choice: "))

    if choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice: "))

    if choice == 1:
        choiceName = "Rock"
    elif choice == 2:
        choiceName = "Paper"
    else:
        choiceName = "Scissors"

    print("User choice is : " + choiceName)
    print("Now its computer s Turn...")

    compChoice = random.randint(1, 3)

    if choice > 3 or choice < 1:
        print("Enter again")

    if compChoice == 1:
        compChoice_name = 'Rock'
    elif compChoice == 2:
        compChoice_name = 'Paper'
    else:
        comChoice_name = 'Scissors'

    print("Computer choice is: " + compChoice_name)
    print(choiceName, 'vs', compChoice_name)

    if choice == compChoice:
        result = "DRAW"
    elif (choice == 1 and compChoice == 2) or (compChoice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and compChoice == 3) or (compChoice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and compChoice == 3) or (compChoice == 2 and choice == 3):
        result = 'Scissors'

    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choiceName:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
    print("Thanks for playing!")

import random

while True:

    print("Enter your choice: \n 1> ROCK \n 2> PAPER \n 3> SCISSORS \n")
    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print("User choice is ->", choice_name)

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is ->", comp_choice_name)

    print(choice_name, 'Vs', comp_choice_name)
    
    if choice == comp_choice:
        print('Its a Draw')
        result = "DRAW"
    if (choice == 1 and comp_choice == 2):
        print('paper wins ')
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins ')
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins')
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins\n')
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins')
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins')
        result = 'Rock'
    if result == 'DRAW':
        print("It's a tie")
    if result == choice_name:
        print("User wins\n")
    else:
        print("Computer wins\n")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing :))")


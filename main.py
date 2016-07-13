import random
play_again = 1

while play_again == 1:
    human_choice = None
    a_dict = {1:"Rock",2:"Paper",3:"Scissors"}
    computer_choice = random.choice([1,2,3])
    while human_choice not in [1,2,3]:
        try:
            human_choice = input("Choose either rock (1), paper (2) or scissors(3): ")
        except NameError:
            pass
    print("You draw: " + a_dict[human_choice])
    print("Herb the Robot drew: " + a_dict[computer_choice])
    
    if computer_choice == human_choice:
        print("It's a tie!")
    print("===")
    try:
        play_again = input("Do you wish to play again? Type 1 for Yes and anything else for No: ")
    except NameError:
        break
    print("===")
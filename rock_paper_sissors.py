import random


def play():
    options = ['R', 'P', "S"]
    user = ''
    while user != 'R' or user != 'P' or user != 'S':
        user = input("Type 'R' for rock, 'P' for paper, or 'S' for scissors: ").upper()
        computer = random.choice(options)
        if user == computer:
            print('Tie!')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        elif user == 'R' and computer == 'P':
            print('Computer wins!')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        if user == 'P' and computer == 'S':
            print('Computer wins')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        elif user == 'P' and computer == 'R':
            print('You win!')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        elif user == 'S' and computer == 'P':
            print('You win!')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        elif user == 'S' and computer == 'R':
            print('Computer wins!')
            play_again = input('Do you want to play again? y/n: ')
            if play_again == 'y':
                play()
            else:
                print("Bye!")
        else:
            print("That's not right enter 'R', 'P', or 'S'")


play()

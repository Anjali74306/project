from random import randint


def win():
    print ('You win!')

def lose():
    print ('You lose!')

i=True
while i:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    random_move=randint(0,2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]

    if player_choice == computer_choice:
        print ('Draw!')
        i=False
    elif player_choice=='rock' and computer_choice == 'scissors':
        win()
        i=True
    elif player_choice=='paper' and computer_choice == 'scissors':
        win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
        i=False
    elif player_choice== 'scissors' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice =='rock'  and computer_choice =='paper' :
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'yes':
        print("continue your game ")
        i=True
    else:
        print("game over")
        i=False


# import random
# while True:
#     print("make your guess:",end=" ")
# guess=str(input())
# guess=guess.lower()
# choices=['rock','paper','seccior']
# computer_choice=choices[random.randint(0,len(random.choices-1))]
# if choice=='rock':
#     if computer_choice=="rock":
#         print("it is tie")
#     elif computer_choice=="paper":
#         print("you lose,sorry:")
#     elif computer_choice=='scissors':
#         print("you win!!!!!! congratts")
# if choice=="paper":
#     if computer_choice=="rock":
#         print("it is tie:")
#     elif computer_choice=="paper":
#         print("you loose,sorry:")
#     elif computer_choice=="scissor":
#         print("you win!!!! congrtas")

import random
def play(player_score,cpu_score):
    while True:
        choices = ("Rock", "Paper", "Scissors", "End")
        computer = choices[random.randint(0,2)] #the computer randonly choose a number form 0-2
        print("Choose")
        print("1 for Rock")
        print("2 for Paper")
        print("3 for Scissors")
        print("4 for End")
        pick = int(input())-1 #reduce 1 to match the list index. ex: if they choose 1 it'll be paper on ourside but to them they chose Rock
        if pick >=4 or pick < 0:
            print("Choose proper vaules!!")
            continue
        player = choices[pick] #Player has to choose from the list of items that represent choices
        ## Conditions of Rock,Paper,Scissors
        if player != 'End':
            print(f"You chose {player}")##f allows you to print variable data inside the string notataion
            print(f"Computer chose {computer}")
        if player == computer:
            print("Its a tie!")
        elif player == 'Rock':
            if computer == 'Paper':
                print("You lose!", computer, "covers", player)
                cpu_score+=1
            else:
                print("You win!", player, "crushed", computer)
                player_score+=1
        elif player == 'Paper':
            if computer == 'Rock':
                print("You win!", player, "covers", computer)
                player_score+=1
            else:
                print("You lose!", computer, "crushed", player)
                cpu_score=+1
        elif player == 'Scissors':
            if computer == 'Rock':
                print("You lose!", computer, "crushed", player)
                cpu_score+=1
            else:
                print("You win!", player, "split", computer)
                player_score=+1
        elif player == 'End':
            print('Good Game!')
            print("Final Scores:")
            print(f"CPU: {cpu_score}")
            print(f"Player: {player_score}")
            break

print("Game is Starting")
play(0,0)
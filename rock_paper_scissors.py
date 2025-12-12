import random
print("WELCOME TO THE GAME OF ROCK PAPER SCISSORS")
print("COMPUTER VS PLAYER ")
options=["rock","paper","scissor"]

rounds=int(input("enter the number of rounds you want to play: "))
print("LET'S START THE GAME!")


player_score = 0
computer_score = 0
ties = 0
next_round=0

for i in range(1, rounds + 1):
    
        player=input("select the choice from (rock paper scissor) or quit to exit the game: ").lower()
        if player=="quit":
            print("YOU QUIT THE GAME EARLY")
            break
            
        while player not in options:
            player=input(" You have choosen invalid option! please select the choice from rock paper scissor or quit: ").lower()
        if player=="quit":
            print("YOU QUIT THE GAME EARLY")
            break
        if player=="quit":
            print("YOU QUIT THE GAME EARLY")
            break
        computer=random.choice(options)
        
        print(f" computer:{computer}")
        print(f" player:{player}")
            
        if computer==player:
            print("IT'S A TIE")
            ties+=1

        elif (computer=="rock" and player=="paper") or \
             (computer=="paper" and player=="scissor") or \
             (computer=="scissor" and player=="rock"):
             print("YOU WON!")
             player_score += 1
        
        else:
            print("YOU LOSE!")
            computer_score+=1
    
print("\n----------THANK YOU FOR PLAYING THE GAME------------")
print(f"ROUNDS COMPLETED: {i if player != 'quit' else i-1}")
print(f"PLAYER SCORE:   {player_score}")
print(f"COMPUTER SCORE: {computer_score}")
print(f"TIES:           {ties}")

if player_score > computer_score:
    print("CONGRATULATIONS! YOU ARE THE OVERALL WINNER!")
elif computer_score > player_score:
    print("THE COMPUTER WINS OVERALL!")
else:
    print("IT'S AN OVERALL TIE!")

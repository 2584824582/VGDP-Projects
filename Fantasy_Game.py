import random
import time
from NHLTeams import *
import NHLTeams
def rules():
    print("You will play against me in a game of NHL Fantasy!")
    time.sleep(3)
    print("I will draw a random team from the list of teams.")
    time.sleep(3)
    print("The team that I pick will be the first team that I pick a player from.")
    time.sleep(3)
    print("Then I will pick another team and you pick a player from that team.")
    time.sleep(3)
    print("Once a player is picked, neither team can pick that same player again.")
    time.sleep(3)
    print("At the end, I will give you a link to ChatGPT and it will pick a winner!")
    game()
def playerPrint():
    global players
    if randomTeamChoice == "Ducks":
        if your_position == "C":
            players = DucksC
def game():
    global randomTeamChoice
    global your_position
    print("I'll draw a team.")
    time.sleep(2)
    randomTeamChoice = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice}.")
    time.sleep(2)
    print("You pick a position.")
    time.sleep(2)
    print("Which position do you want to pick: (C, RW, LW, DEF, G) ")
    your_position = input()
    print(f"You picked: {your_position}.")
    time.sleep(2)
    availablePlayers = randomTeamChoice + your_position
    if hasattr(NHLTeams, availablePlayers):
        print(f"Here are the available players: {getattr(NHLTeams, availablePlayers)}")
    time.sleep(2)
    print("Which player do you want to pick?")
    time.sleep(2)
    player = input()
    print(f"You picked: {player}.")
    time.sleep(2)
    used_players.append(player)

#Start the game
print("Welcome to Fantasy!")
time.sleep(1)
print("If you know the rules, you can skip this.")
time.sleep(1)
input1 = input("Do you know the rules? Y/N: ")
if input1 == "N" or input1 == "n":
    rules()
elif input1 == "Y" or input1 == "y":
    print("Great! Let's begin!")
    time.sleep(1)
    game()
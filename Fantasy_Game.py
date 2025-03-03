import random
import time
from NHLTeams import *
import NHLTeams
#import openai

def Teamlister1():
    print(team1)

def Teamlister2():
    print(team2)

def ListPositionPlayers():
    if availablePlayers in globals():
        print(f"Here are the available players: {globals()[availablePlayers]}.")
def checkplayersUser():
    if player1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(2)
    elif player1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(2)
        checkplayersUser()

def checkplayersAI():
    global aiplayer1
    availablePlayers = randomTeamChoice + randomPosition1
    if availablePlayers in globals():
        print(f"Here are the available players: {globals()[availablePlayers]}.")
        aiplayer1 = random.choice(globals()[availablePlayers])
        time.sleep(2)

def skipTeam():
    skip = 1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(2)
        print(f"You have {skip} skips left.") 
        time.sleep(2)
        print("I'll draw a team for you.")
        time.sleep(2)
        randomTeamChoice = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(2)
        print(f"You have {skip} skips left.") 
        time.sleep(2)
def rules():
    print("You will play against me in a playerPick1 of NHL Fantasy!")
    time.sleep(3)
    print("I will draw a random team from the list of teams.")
    time.sleep(3)
    print("The team that I pick will be the first team that I pick a player from.")
    time.sleep(3)
    print("Then I will pick another team and you pick a player from that team.")
    time.sleep(3)
    print("Once a player is picked, neither team can pick that same player again.")
    time.sleep(3)
    print("You will get one skip if you don't ike the team that is picked.")
    time.sleep(3)
    print("At the end, I will give you a link to ChatGPT and it will pick a winner!")
    playerPick1()

def playerPick1():
    global randomTeamChoice
    global your_position1
    global player1
    global availablePlayers
    print("I'll draw a team for you.")
    time.sleep(2)
    randomTeamChoice = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice}.")
    time.sleep(2)
    skipTeam()
    print("You pick a position.")
    time.sleep(2)
    print("Which position do you want to pick: (C, RW, LW, Def, G) ")
    your_position1 = input()
    print(f"You picked: {your_position1}.")
    time.sleep(2)
    availablePlayers = randomTeamChoice + your_position1
    ListPositionPlayers()
    print("Which player do you want to pick?")
    time.sleep(2)
    player1 = input()
    checkplayersUser()
    print(f"You picked {player1} as your {your_position1}.")
    time.sleep(2)
    used_players.append(player1)
    team1.append(player1)
    used_Positions1.append(your_position1)
    time.sleep(2)
    print("Here is your team so far:")
    time.sleep(2)
    Teamlister1()
    time.sleep(2)
    AIPick1()

def AIPick1():
    global randomPosition1
    print("I'll draw a team for me.")
    time.sleep(2)
    randomTeamChoice = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice}.")
    time.sleep(2)
    print("I will now pick a position.")
    randomPosition1 = random.choice(positions)
    print(f"I picked: {randomPosition1}.")
    time.sleep(2)
    checkplayersAI()
    print(f"I picked {aiplayer1} as my {randomPosition1}.")
    time.sleep(2)
    used_players.append(aiplayer1)
    team2.append(aiplayer1)
    used_Positions2.append(randomPosition1)
    time.sleep(2)
    print("Here is my team so far:")
    time.sleep(2)
    Teamlister2()



    

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
    playerPick1()

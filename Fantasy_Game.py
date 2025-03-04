import random
import time
from NHLTeams import *
import NHLTeams
#Individual Variables
skip = 1
#All Fucntions for Player and AI
def rulesAI():
    print("You will play against me in a game of NHL Fantasy!")
    time.sleep(3)
    print("I will draw a random team from the list of teams.")
    time.sleep(3)
    print("The team that I pick will be the first team that you pick a player from.")
    time.sleep(3)
    print("Then I will pick another team and I will pick a player from that team.")
    time.sleep(3)
    print("Once a player is picked, neither team can pick that same player again.")
    time.sleep(3)
    print("You will get one skip per game.")
    time.sleep(3)
    print("At the end, ChatGPT will pick a winner!")
    time.sleep(3)
    print("Good Luck!")
    playerPick1()

def rulesUsersONLY():
    print("You will play against each other in a game of NHL Fantasy!")
    time.sleep(3)
    print("I will draw a random team from the list of teams.")
    time.sleep(3)
    print("The team that I pick will be the first team that player 1 picks a player from.")
    time.sleep(3)
    print("Then I will pick another team and player 2 will pick a player from that team.")
    time.sleep(3)
    print("Once a player is picked, neither player can pick that same player again.")
    time.sleep(3)
    print("You will get one skip per game.")
    time.sleep(3)
    print("At the end, ChatGPT will pick a winner!")
    time.sleep(3)
    print("Good Luck!")
    playerPick1()

def skipTeamOnePlayer():
    global skip
    global randomTeamChoice
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamOnePlayer2():
    global skip
    global randomTeamChoice2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice2 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamOnePlayer3():
    global skip
    global randomTeamChoice3
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice3 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice3}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)  

def skipTeamOnePlayer4():
    global skip
    global randomTeamChoice4
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice4 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice4}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamOnePlayer5():
    global skip
    global randomTeamChoice5
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice5 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice5}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamOnePlayer6():
    global skip
    global randomTeamChoice6
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice6 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice6}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def checkpositionUser():
    if your_position not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition1()

def checkpositionUser2():
    if your_position2 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position2 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition2()

def checkpositionUser3():
    if your_position3 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position3 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition3()

def checkpositionUser4():
    if your_position4 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position4 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition4()

def checkpositionUser5():
    if your_position5 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position5 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition5()

def checkpositionUser6():
    if your_position6 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position6 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition6()

def redoPosition1():
    global your_position
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position = input()
    checkpositionUser()

def redoPosition2():
    global your_position2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position2 = input()
    checkpositionUser2()

def redoPosition3():
    global your_position3
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position3 = input()
    checkpositionUser3()

def redoPosition4():
    global your_position4
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position4 = input()
    checkpositionUser4()

def redoPosition5():
    global your_position5
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position5 = input()
    checkpositionUser5()

def redoPosition6():
    global your_position6
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position6 = input()
    checkpositionUser6()

def ListPositionPlayersOnePlayer():
    availablePlayers = randomTeamChoice + your_position
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")

def ListPositionPlayers2OnePlayer():
    availablePlayers2 = randomTeamChoice2 + your_position2
    if availablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers3OnePlayer():
    availablePlayers3 = randomTeamChoice3 + your_position3
    if availablePlayers3 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers3]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers4OnePlayer():
    availablePlayers4 = randomTeamChoice4 + your_position4
    if availablePlayers4 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers4]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers5OnePlayer():
    availablePlayers5 = randomTeamChoice5 + your_position5
    if availablePlayers5 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers5]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers6OnePlayer():
    availablePlayers6 = randomTeamChoice6 + your_position6
    if availablePlayers6 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers6]}.")
        print("Which player do you want to pick?")

def checkplayersUser():
    if player not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersOnePlayer()

def checkplayersUser2():
    if player2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers2OnePlayer()

def checkplayersUser3():
    if player3 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player3 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers3OnePlayer()

def checkplayersUser4():
    if player4 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player4 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers4OnePlayer()

def checkplayersUser5():
    if player5 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player5 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers5OnePlayer()

def checkplayersUser6():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers6OnePlayer()

def checkPositionAI():
    global randomPosition
    randomPosition = random.choice(positionsAI)
    if randomPosition in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI()

def checkPositionAI2():
    global randomPosition2
    randomPosition2 = random.choice(positionsAI)
    if randomPosition2 in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI2()

def checkPositionAI3():
    global randomPosition3
    randomPosition3 = random.choice(positionsAI)
    if randomPosition3 in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI3()

def checkPositionAI4():
    global randomPosition4
    randomPosition4 = random.choice(positionsAI)
    if randomPosition4 in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI4()
        
def checkPositionAI5():
    global randomPosition5
    randomPosition5 = random.choice(positionsAI)
    if randomPosition5 in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI5()
        
def checkPositionAI6():
    global randomPosition6
    randomPosition6 = random.choice(positionsAI)
    if randomPosition6 in NHLTeams.used_Positions2:
        print("I picked a position that has already been used. Let me pick again.")
        time.sleep(1)
        checkPositionAI6()

def checkplayersAI():
    global AiPlayer1
    availablePlayers = randomTeamChoiceAI + randomPosition
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer1 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def checkplayersAI2():
    global AiPlayer2
    availablePlayers = randomTeamChoiceAI + randomPosition2
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer2 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def checkplayersAI3():
    global AiPlayer3
    availablePlayers = randomTeamChoiceAI + randomPosition3
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer3 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def checkplayersAI4():
    global AiPlayer4
    availablePlayers = randomTeamChoiceAI + randomPosition4
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer4 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def checkplayersAI5():
    global AiPlayer5
    availablePlayers = randomTeamChoiceAI + randomPosition5
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer5 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def checkplayersAI6():
    global AiPlayer6
    availablePlayers = randomTeamChoiceAI + randomPosition6
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")
        AiPlayer6 = random.choice(globals()[availablePlayers])
        time.sleep(1)

def playerPick1():
    global randomTeamChoice
    global your_position
    global player
    global availablePlayers
    print("Round 1")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice}.")
    time.sleep(1)
    skipTeamOnePlayer()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position = input()
    time.sleep(1)
    checkpositionUser()
    print(f"You picked: {your_position}.")
    time.sleep(1)
    availablePlayers = randomTeamChoice + your_position
    ListPositionPlayersOnePlayer()
    print("Which player do you want to pick?")
    time.sleep(1)
    player = input()
    checkplayersUser()
    time.sleep(1)
    print(f"You picked {player} as your {your_position}.")
    time.sleep(1)
    used_players.append(player)
    used_Positions1.append(your_position)
    positionsUser1.remove(your_position)
    time.sleep(1)
    AIPick1()
    time.sleep(1)

def AIPick1():
    global randomPosition
    global randomTeamChoiceAI
    global AiPlayer1
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI()
    time.sleep(1)
    print(f"I picked: {randomPosition}.")
    time.sleep(1)
    checkplayersAI()
    time.sleep(1)
    print(f"I picked {AiPlayer1} as my {randomPosition}.")
    time.sleep(1)
    used_players.append(AiPlayer1)
    used_Positions2.append(randomPosition)
    positionsAI.remove(randomPosition)
    time.sleep(1)
    playerPick2()

def playerPick2():
    global availablePlayers2
    global your_position2
    global player2
    global randomTeamChoice2
    print("Round 2")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice2 = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice2}.")
    time.sleep(1)
    skipTeamOnePlayer2()
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position2 = input()
    checkpositionUser2()
    print(f"You picked: {your_position2}.")
    availablePlayers2 = randomTeamChoice2 + your_position2
    ListPositionPlayers2OnePlayer()
    time.sleep(1)
    player2 = input()
    checkplayersUser2()
    time.sleep(1)
    print(f"You picked {player2} as your {your_position2}.")
    time.sleep(1)
    used_players.append(player2)
    used_Positions1.append(your_position2)
    positionsUser1.remove(your_position2)
    time.sleep(1)
    AIpick2()

def AIpick2():
    global randomPosition2
    global randomTeamChoiceAI
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI2()
    time.sleep(1)
    print(f"I picked: {randomPosition2}.")
    time.sleep(1)
    checkplayersAI2()
    time.sleep(1)
    print(f"I picked {AiPlayer2} as my {randomPosition2}.")
    time.sleep(1)
    used_players.append(AiPlayer2)
    used_Positions2.append(randomPosition2)
    positionsAI.remove(randomPosition2)
    time.sleep(1)
    playerPick3()

def playerPick3():
    global availablePlayers3
    global your_position3
    global player3
    global randomTeamChoice3
    print("Round 3")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice3 = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice3}.")
    time.sleep(1)
    skipTeamOnePlayer3()
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position3 = input()
    checkpositionUser3()
    print(f"You picked: {your_position3}.")
    availablePlayers3 = randomTeamChoice3 + your_position3
    ListPositionPlayers3OnePlayer()
    time.sleep(1)
    player3 = input()
    checkplayersUser3()
    time.sleep(1)
    print(f"You picked {player3} as your {your_position3}.")
    time.sleep(1)
    used_players.append(player3)
    used_Positions1.append(your_position3)
    positionsUser1.remove(your_position3)
    time.sleep(1)
    AIpick3()

def AIpick3():
    global randomPosition3
    global randomTeamChoiceAI
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI3()
    time.sleep(1)
    print(f"I picked: {randomPosition3}.")
    time.sleep(1)
    checkplayersAI3()
    time.sleep(1)
    print(f"I picked {AiPlayer3} as my {randomPosition3}.")
    time.sleep(1)
    used_players.append(AiPlayer3)
    used_Positions2.append(randomPosition3)
    positionsAI.remove(randomPosition3)
    time.sleep(1)
    playerPick4()

def playerPick4():
    global availablePlayers4
    global your_position4
    global player4
    global randomTeamChoice4
    print("Round 4")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice4 = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice4}.")
    time.sleep(1)
    skipTeamOnePlayer4()
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position4 = input()
    checkpositionUser4()
    print(f"You picked: {your_position4}.")
    availablePlayers4 = randomTeamChoice4 + your_position4
    ListPositionPlayers4OnePlayer()
    time.sleep(1)
    player4 = input()
    checkplayersUser4()
    time.sleep(1)
    print(f"You picked {player4} as your {your_position4}.")
    time.sleep(1)
    used_players.append(player4)
    used_Positions1.append(your_position4)
    positionsUser1.remove(your_position4)
    time.sleep(1)
    AIpick4()

def AIpick4():
    global randomPosition4
    global randomTeamChoiceAI
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI4()
    time.sleep(1)
    print(f"I picked: {randomPosition4}.")
    time.sleep(1)
    checkplayersAI4()
    time.sleep(1)
    print(f"I picked {AiPlayer4} as my {randomPosition4}.")
    time.sleep(1)
    used_players.append(AiPlayer4)
    used_Positions2.append(randomPosition4)
    positionsAI.remove(randomPosition4)
    time.sleep(1)
    playerPick5()

def playerPick5():
    global availablePlayers5
    global your_position5
    global player5
    global randomTeamChoice5
    print("Round 5")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice5 = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice5}.")
    time.sleep(1)
    skipTeamOnePlayer5()
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position5 = input()
    checkpositionUser5()
    print(f"You picked: {your_position5}.")
    availablePlayers5 = randomTeamChoice5 + your_position5
    ListPositionPlayers5OnePlayer()
    time.sleep(1)
    player5 = input()
    checkplayersUser5()
    time.sleep(1)
    print(f"You picked {player5} as your {your_position5}.")
    time.sleep(1)
    used_players.append(player5)
    used_Positions1.append(your_position5)
    positionsUser1.remove(your_position5)
    time.sleep(1)
    AIpick5()

def AIpick5():
    global randomPosition5
    global randomTeamChoiceAI
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI5()
    time.sleep(1)
    print(f"I picked: {randomPosition5}.")
    time.sleep(1)
    checkplayersAI5()
    time.sleep(1)
    print(f"I picked {AiPlayer5} as my {randomPosition5}.")
    time.sleep(1)
    used_players.append(AiPlayer5)
    used_Positions2.append(randomPosition5)
    positionsAI.remove(randomPosition5)
    time.sleep(1)
    playerPick6()

def playerPick6():
    global availablePlayers6
    global your_position6
    global player6
    global randomTeamChoice6
    print("Round 6")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    randomTeamChoice6 = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoice6}.")
    time.sleep(1)
    skipTeamOnePlayer6()
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position6 = input()
    checkpositionUser6()
    print(f"You picked: {your_position6}.")
    availablePlayers6 = randomTeamChoice6 + your_position6
    ListPositionPlayers6OnePlayer()
    time.sleep(1)
    player6 = input()
    checkplayersUser6()
    time.sleep(1)
    print(f"You picked {player6} as your {your_position6}.")
    time.sleep(1)
    used_players.append(player6)
    used_Positions1.append(your_position6)
    positionsUser1.remove(your_position6)
    time.sleep(1)
    print("Here is your Final Team: ")
    Teamlister1()
    AIpick6()

def AIpick6():
    global randomPosition6
    global randomTeamChoiceAI
    print("I'll draw a team for me.")
    time.sleep(1)
    randomTeamChoiceAI = random.choice(teams)
    print(f"The team I picked is: {randomTeamChoiceAI}.")
    time.sleep(1)
    print("I will now pick a position.")
    checkPositionAI6()
    time.sleep(1)
    print(f"I picked: {randomPosition6}.")
    time.sleep(1)
    checkplayersAI6()
    time.sleep(1)
    print(f"I picked {AiPlayer6} as my {randomPosition6}.")
    time.sleep(1)
    used_players.append(AiPlayer6)
    used_Positions2.append(randomPosition6)
    positionsAI.remove(randomPosition6)
    time.sleep(1)
    print("Here is my Final Team: ")
    Teamlister2()
    time.sleep(1)
    print("Put these teams into chatGPT.com and let it pick a winner!")
    Winner()

def Teamlister1():
    global PlayerTeam
    PlayerTeam =  player + " as your " + your_position, player2 + " as your " + your_position2,player3 + " as your " + your_position3,player4 + " as your " + your_position4,player5 + " as your " + your_position5,player6 + " as your " + your_position6
    print(PlayerTeam)

def Teamlister2():
    global AITeam
    AITeam =  AiPlayer1 + " as my " + randomPosition, AiPlayer2 + " as my " + randomPosition2, AiPlayer3 + " as my " + randomPosition3, AiPlayer4 + " as my " + randomPosition4, AiPlayer5 + " as my " + randomPosition5, AiPlayer6 + " as my " + randomPosition6
    print(AITeam)

def Winner():
    print("Who won the game? Team1 or Team2?")
    winner = input()
    if winner == "Team1":
        time.sleep(1)
        print("Congratulations! You won the game!")
    elif winner == "Team2":
        time.sleep(1)
        print("I won the game! Better luck next time!")

#All functions for 2 Players
def skipTeamTwoPlayersplayer11():
    global skip
    global firstTeamChoiceplayer1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        firstTeamChoiceplayer1 = random.choice(teams)
        print(f"The team I picked is: {firstTeamChoiceplayer1}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers12():
    global skip
    global secondTeamChoiceplayer1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        secondTeamChoiceplayer1 = random.choice(teams)
        print(f"The team I picked is: {secondTeamChoiceplayer1}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers13():
    global skip
    global thirdTeamChoiceplayer1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        thirdTeamChoiceplayer1 = random.choice(teams)
        print(f"The team I picked is: {thirdTeamChoiceplayer1}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)  

def skipTeamTwoPlayers14():
    global skip
    global fourthTeamChoiceplayer1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        fourthTeamChoiceplayer1 = random.choice(teams)
        print(f"The team I picked is: {fourthTeamChoiceplayer1}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers15():
    global skip
    global fifthTeamChoiceplayer1
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        fifthTeamChoiceplayer1 = random.choice(teams)
        print(f"The team I picked is: {fifthTeamChoiceplayer1}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers16():
    global skip
    global randomTeamChoice6
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice6 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice6}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayersPlayer21():
    global skip
    global firstTeamChoiceplayer2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        firstTeamChoiceplayer2 = random.choice(teams)
        print(f"The team I picked is: {firstTeamChoiceplayer2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers2Player22():
    global skip
    global secondTeamChoiceplayer2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        secondTeamChoiceplayer2 = random.choice(teams)
        print(f"The team I picked is: {secondTeamChoiceplayer2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers3Player23():
    global skip
    global thirdTeamChoiceplayer2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        thirdTeamChoiceplayer2 = random.choice(teams)
        print(f"The team I picked is: {thirdTeamChoiceplayer2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)  

def skipTeamTwoPlayers4Player24():
    global skip
    global fourthTeamChoiceplayer2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        fourthTeamChoiceplayer2 = random.choice(teams)
        print(f"The team I picked is: {fourthTeamChoiceplayer2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers5Player25():
    global skip
    global fifthTeamChoiceplayer2
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        fifthTeamChoiceplayer2 = random.choice(teams)
        print(f"The team I picked is: {fifthTeamChoiceplayer2}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def skipTeamTwoPlayers6Player26():
    global skip
    global randomTeamChoice6
    print("Do you want to skip this team? Y/N")
    skipchoice = input()
    if skipchoice == "Y" or skipchoice == "y" and skip == 1:
        skip = 0
        print("You skipped this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.")
        print("I'll draw a team for you.")
        time.sleep(1)
        randomTeamChoice6 = random.choice(teams)
        print(f"The team I picked is: {randomTeamChoice6}.")
    elif skipchoice == "N" or skipchoice == "n":
        print("You didn't skip this team.")
        time.sleep(1)
        print(f"You have {skip} skips left.") 
        time.sleep(1)
    if skip == 0 and skipchoice == "Y" or skipchoice == "y":
        print("You have no more skips left.")
        time.sleep(1)

def ListPositionPlayersTwoPlayers11():
    firstTeamAvailablePlayers = firstTeamChoiceplayer1 + firstyour_positionplayer1
    if firstTeamAvailablePlayers in globals():
        print(f"Here are the applicable players: {globals()[firstTeamAvailablePlayers]}.")

def ListPositionPlayers2TwoPlayers12():
    secondTeamAvailablePlayers1 = firstTeamChoiceplayer2 + firstyour_positionplayer2
    if secondTeamAvailablePlayers1 in globals():
        print(f"Here are the applicable players: {globals()[secondTeamAvailablePlayers1]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers3TwoPlayers13():
    thirdTeamAvailablePlayers1 = thirdTeamChoiceplayer1 + thirdyour_positionplayer1
    if thirdTeamAvailablePlayers1 in globals():
        print(f"Here are the applicable players: {globals()[thirdTeamAvailablePlayers1]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers4TwoPlayers14():
    fourthTeamAvailablePlayers1 = fourthTeamChoiceplayer1 + fourthyour_positionplayer1
    if fourthTeamAvailablePlayers1 in globals():
        print(f"Here are the applicable players: {globals()[fourthTeamAvailablePlayers1]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers5TwoPlayers15():
    fifthTeamAvailablePlayers1 = fifthTeamChoiceplayer1 + fifthyour_positionplayer1
    if fifthTeamAvailablePlayers1 in globals():
        print(f"Here are the applicable players: {globals()[fifthTeamAvailablePlayers1]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers6TwoPlayers16():
    availablePlayers6 = randomTeamChoice6 + your_position6
    if availablePlayers6 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers6]}.")
        print("Which player do you want to pick?")

def ListPositionPlayersTwoPlayers21():
    firstTeamAvailablePlayers2 = firstTeamChoiceplayer2 + firstyour_positionplayer2
    if firstTeamAvailablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[firstTeamAvailablePlayers2]}.")

def ListPositionPlayers2TwoPlayers22():
    secondTeamAvailablePlayers2 = secondTeamChoiceplayer2 + secondyour_positionplayer2
    if secondTeamAvailablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[secondTeamAvailablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers3TwoPlayers23():
    thirdTeamAvailablePlayers2 = thirdTeamChoiceplayer2 + thirdyour_positionplayer2
    if thirdTeamAvailablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[thirdTeamAvailablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers4TwoPlayers24():
    fourthTeamAvailablePlayers2 = fourthTeamChoiceplayer2 + fourthyour_positionplayer2
    if fourthTeamAvailablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[fourthTeamAvailablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers5TwoPlayers25():
    fifthTeamAvailablePlayers2 = fifthTeamChoiceplayer2 + fifthyour_positionplayer2
    if fifthTeamAvailablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[fifthTeamAvailablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers6TwoPlayers26():
    availablePlayers6 = randomTeamChoice6 + your_position6
    if availablePlayers6 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers6]}.")
        print("Which player do you want to pick?")

def checkpositionUserPlayer11():
    if firstyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif firstyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer11()

def checkpositionUserPlayer12():
    if secondyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif secondyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer12()

def checkpositionUserPlayer13():
    if thirdyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif thirdyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition3()

def checkpositionUserPlayer14():
    if fourthyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif fourthyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition4()

def checkpositionUserPlayer15():
    if fifthyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif fifthyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition5()

def checkpositionUserPlayer16():
    if your_position6 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position6 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition6()

def checkpositionUserplayer21():
    if firstyour_positionplayer2 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif firstyour_positionplayer2 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer21()

def checkpositionUserplayer22():
    if secondyour_positionplayer2 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif secondyour_positionplayer2 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer22()

def checkpositionUserplayer23():
    if thirdyour_positionplayer2 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif thirdyour_positionplayer2 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer23()

def checkpositionUserplayer24():
    if fourthyour_positionplayer2 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif fourthyour_positionplayer2 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer24()

def checkpositionUserplayer25():
    if fifthyour_positionplayer2 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif fifthyour_positionplayer2 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer25()

def checkpositionUserplayer26():
    if your_position6 not in NHLTeams.used_Positions2:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position6 in NHLTeams.used_Positions2:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer26()

def checkplayersUserplayer11():
    if firstplayer1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif firstplayer1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers11()

def checkplayersUserplayer12():
    if secondplayer1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif secondplayer1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers2TwoPlayers12()

def checkplayersUserplayer13():
    if thirdplayer1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif thirdplayer1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers3TwoPlayers13()

def checkplayersUserplayer14():
    if fourthplayer1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif fourthplayer1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers4TwoPlayers14()

def checkplayersUserplayer15():
    if fifthplayer1 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif fifthplayer1 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)   
        ListPositionPlayers5TwoPlayers15()

def checkplayersUserplayer16():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers6TwoPlayers16()

def checkplayersUserplayer21():
    if firstplayer2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif firstplayer2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers21()

def checkplayersUserplayer22():
    if secondplayer2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif secondplayer2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers2TwoPlayers22()

def checkplayersUserplayer23():
    if thirdplayer2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif thirdplayer2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers3TwoPlayers23()

def checkplayersUserplayer24():
    if fourthplayer2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif fourthplayer2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers4TwoPlayers24()

def checkplayersUserplayer25():
    if fifthplayer2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif fifthplayer2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers5TwoPlayers25()

def checkplayersUserplayer26():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers6TwoPlayers26()

def redoPositionplayer11():
    global firstyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer1 = input()
    checkpositionUserPlayer11()

def redoPositionplayer12():
    global firstyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer2 = input()
    checkpositionUserPlayer12()

def redoPositionplayer13():
    global thirdyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    thirdyour_positionplayer1 = input()
    checkpositionUserPlayer13()

def redoPositionplayer14():
    global fourthyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fourthyour_positionplayer1 = input()
    checkpositionUserPlayer14()

def redoPositionplayer15():
    global fifthyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fifthyour_positionplayer1 = input()
    checkpositionUserPlayer15()

def redoPositionplayer16():
    global sixthyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    sixthyour_positionplayer1 = input()
    checkpositionUserPlayer16()

def redoPositionplayer21():
    global firstyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer2 = input()
    checkpositionUserplayer21()

def redoPositionplayer22():
    global secondyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    secondyour_positionplayer2 = input()
    checkpositionUserplayer22()

def redoPositionplayer23():
    global thirdyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    thirdyour_positionplayer2 = input()
    checkpositionUserplayer23()

def redoPositionplayer24():
    global fourthyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fourthyour_positionplayer2 = input()
    checkpositionUserplayer24()

def redoPositionplayer25():
    global fifthyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fifthyour_positionplayer2 = input()
    checkpositionUserplayer25()

def redoPositionplayer26():
    global sixthyour_positionplayer2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    sixthyour_positionplayer2 = input()
    checkpositionUserplayer26()

def player1Pick1():
    global firstTeamChoiceplayer1
    global firstyour_positionplayer1
    global firstplayer1
    global firstTeamAvailablePlayers
    print("Round 1")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    firstTeamChoiceplayer1 = random.choice(teams)
    print(f"The team I picked is: {firstTeamChoiceplayer1}.")
    time.sleep(1)
    skipTeamTwoPlayersplayer11()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer11()
    print(f"You picked: {firstyour_positionplayer1}.")
    time.sleep(1)
    firstTeamAvailablePlayers = firstTeamChoiceplayer1 + firstyour_positionplayer1
    ListPositionPlayersTwoPlayers11()
    print("Which player do you want to pick?")
    time.sleep(1)
    firstplayer1 = input()
    checkplayersUserplayer11()
    time.sleep(1)
    print(f"You picked {firstplayer1} as your {firstyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(firstplayer1)
    used_Positions1.append(firstyour_positionplayer1)
    positionsUser1.remove(firstyour_positionplayer1)
    time.sleep(1)
    player2Pick1()
    time.sleep(1)

def player2Pick1():
    global firstTeamChoiceplayer2
    global firstyour_positionplayer2
    global firstplayer2
    global firstTeamAvailablePlayers2
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    firstTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {firstTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayersPlayer21()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer2 = input()
    time.sleep(1)
    checkpositionUserplayer21()
    print(f"You picked: {firstyour_positionplayer2}.")
    time.sleep(1)
    firstTeamAvailablePlayers2 = firstTeamChoiceplayer2 + firstyour_positionplayer2
    ListPositionPlayersTwoPlayers21()
    print("Which player do you want to pick?")
    time.sleep(1)
    firstplayer2 = input()
    checkplayersUserplayer21()
    time.sleep(1)
    print(f"You picked {firstplayer2} as your {firstyour_positionplayer2}.")
    time.sleep(1)
    used_players.append(firstplayer2)
    used_Positions2.append(firstyour_positionplayer2)
    positionsUser2.remove(firstyour_positionplayer2)
    time.sleep(1)
    player1Pick2()
    time.sleep(1)

def player1Pick2():
    global secondTeamChoiceplayer1
    global secondyour_positionplayer1
    global secondplayer1
    global secondTeamAvailablePlayers1
    print("Round 2")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    firstTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {firstTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayers12()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    secondyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer12()
    print(f"You picked: {secondyour_positionplayer1}.")
    time.sleep(1)
    secondTeamAvailablePlayers1 = firstTeamChoiceplayer2 + secondyour_positionplayer1
    ListPositionPlayers2TwoPlayers12()
    print("Which player do you want to pick?")
    time.sleep(1)
    secondplayer1 = input()
    checkplayersUserplayer12()
    time.sleep(1)
    print(f"You picked {secondplayer1} as your {secondyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(secondplayer1)
    used_Positions1.append(secondyour_positionplayer1)
    positionsUser1.remove(secondyour_positionplayer1)
    time.sleep(1)
    player2Pick2()
    time.sleep(1)

def player2Pick2():
    global secondTeamChoiceplayer2
    global secondyour_positionplayer2
    global secondplayer2
    global secondTeamAvailablePlayers2
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    secondTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {secondTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayers2Player22()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    secondyour_positionplayer2 = input()
    time.sleep(1)
    checkpositionUserplayer22()
    print(f"You picked: {secondyour_positionplayer2}.")
    time.sleep(1)
    secondTeamAvailablePlayers2 = secondTeamChoiceplayer2 + secondyour_positionplayer2
    ListPositionPlayers2TwoPlayers22()
    print("Which player do you want to pick?")
    time.sleep(1)
    secondplayer2 = input()
    checkplayersUserplayer22()
    time.sleep(1)
    print(f"You picked {secondplayer2} as your {secondyour_positionplayer2}.")
    time.sleep(1)
    used_players.append(secondplayer2)
    used_Positions2.append(secondyour_positionplayer2)
    positionsUser2.remove(secondyour_positionplayer2)
    time.sleep(1)
    player1Pick3()
    time.sleep(1)

def player1Pick3():
    global thirdTeamChoiceplayer1
    global thirdyour_positionplayer1
    global thirdplayer1
    global thirdTeamAvailablePlayers1
    print("Round 3")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    thirdTeamChoiceplayer1 = random.choice(teams)
    print(f"The team I picked is: {thirdTeamChoiceplayer1}.")
    time.sleep(1)
    skipTeamTwoPlayers13()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    thirdyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer13()
    print(f"You picked: {thirdyour_positionplayer1}.")
    time.sleep(1)
    thirdTeamAvailablePlayers1 = firstTeamChoiceplayer2 + thirdyour_positionplayer1
    ListPositionPlayers3TwoPlayers13()
    print("Which player do you want to pick?")
    time.sleep(1)
    thirdplayer1 = input()
    checkplayersUserplayer13()
    time.sleep(1)
    print(f"You picked {thirdplayer1} as your {thirdyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(thirdplayer1)
    used_Positions1.append(thirdyour_positionplayer1)
    positionsUser1.remove(thirdyour_positionplayer1)
    time.sleep(1)
    player2Pick3()
    time.sleep(1)

def player2Pick3():
    global thirdTeamChoiceplayer2
    global thirdyour_positionplayer2
    global thirdplayer2
    global thirdTeamAvailablePlayers2
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    thirdTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {thirdTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayers3Player23()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    thirdyour_positionplayer2 = input()
    time.sleep(1)
    checkpositionUserplayer23()
    print(f"You picked: {thirdyour_positionplayer2}.")
    time.sleep(1)
    thirdTeamAvailablePlayers2 = thirdTeamChoiceplayer2 + thirdyour_positionplayer2
    ListPositionPlayers3TwoPlayers23()
    print("Which player do you want to pick?")
    time.sleep(1)
    thirdplayer2 = input()
    checkplayersUserplayer23()
    time.sleep(1)
    print(f"You picked {thirdplayer2} as your {thirdyour_positionplayer2}.")
    time.sleep(1)
    used_players.append(thirdplayer2)
    used_Positions2.append(thirdyour_positionplayer2)
    positionsUser2.remove(thirdyour_positionplayer2)
    time.sleep(1)
    player1Pick4()
    time.sleep(1)

def player1Pick4():
    global fourthTeamChoiceplayer1
    global fourthyour_positionplayer1
    global fourthplayer1
    global fourthTeamAvailablePlayers1
    print("Round 4")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    fourthTeamChoiceplayer1 = random.choice(teams)
    print(f"The team I picked is: {fourthTeamChoiceplayer1}.")
    time.sleep(1)
    skipTeamTwoPlayers14()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fourthyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer14()
    print(f"You picked: {fourthyour_positionplayer1}.")
    time.sleep(1)
    fourthTeamAvailablePlayers1 = firstTeamChoiceplayer2 + fourthyour_positionplayer1
    ListPositionPlayers4TwoPlayers14()
    print("Which player do you want to pick?")
    time.sleep(1)
    fourthplayer1 = input()
    checkplayersUserplayer14()
    time.sleep(1)
    print(f"You picked {fourthplayer1} as your {fourthyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(fourthplayer1)
    used_Positions1.append(fourthyour_positionplayer1)
    positionsUser1.remove(fourthyour_positionplayer1)
    time.sleep(1)
    player2Pick4()
    time.sleep(1)

def player2Pick4():
    global fourthTeamChoiceplayer2
    global fourthyour_positionplayer2
    global fourthplayer2
    global fourthTeamAvailablePlayers2
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    fourthTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {fourthTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayers4Player24()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fourthyour_positionplayer2 = input()
    time.sleep(1)
    checkpositionUserplayer24()
    print(f"You picked: {fourthyour_positionplayer2}.")
    time.sleep(1)
    fourthTeamAvailablePlayers2 = fourthTeamChoiceplayer2 + fourthyour_positionplayer2
    ListPositionPlayers4TwoPlayers24()
    print("Which player do you want to pick?")
    time.sleep(1)
    fourthplayer2 = input()
    checkplayersUserplayer24()
    time.sleep(1)
    print(f"You picked {fourthplayer2} as your {fourthyour_positionplayer2}.")
    time.sleep(1)
    used_players.append(fourthplayer2)
    used_Positions2.append(fourthyour_positionplayer2)
    positionsUser2.remove(fourthyour_positionplayer2)
    time.sleep(1)
    player1Pick5()
    time.sleep(1)

def player1Pick5():
    global fifthTeamChoiceplayer1
    global fifthyour_positionplayer1
    global fifthplayer1
    global fifthTeamAvailablePlayers1
    print("Round 5")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    fifthTeamChoiceplayer1 = random.choice(teams)
    print(f"The team I picked is: {fifthTeamChoiceplayer1}.")
    time.sleep(1)
    skipTeamTwoPlayers15()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fifthyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer15()
    print(f"You picked: {fifthyour_positionplayer1}.")
    time.sleep(1)
    fifthTeamAvailablePlayers1 = firstTeamChoiceplayer2 + fifthyour_positionplayer1
    ListPositionPlayers5TwoPlayers15()
    print("Which player do you want to pick?")
    time.sleep(1)
    fifthplayer1 = input()
    checkplayersUserplayer15()
    time.sleep(1)
    print(f"You picked {fifthplayer1} as your {fifthyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(fifthplayer1)
    used_Positions1.append(fifthyour_positionplayer1)
    positionsUser1.remove(fourthyour_positionplayer1)
    time.sleep(1)
    player2Pick5()
    time.sleep(1)

def player2Pick5():
    global fifthTeamChoiceplayer2
    global fifthyour_positionplayer2
    global fifthplayer2
    global fifthTeamAvailablePlayers2
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    fifthTeamChoiceplayer2 = random.choice(teams)
    print(f"The team I picked is: {fifthTeamChoiceplayer2}.")
    time.sleep(1)
    skipTeamTwoPlayers5Player25()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    fifthyour_positionplayer2 = input()
    time.sleep(1)
    checkpositionUserplayer25()
    print(f"You picked: {fifthyour_positionplayer2}.")
    time.sleep(1)
    fifthTeamAvailablePlayers2 = fourthTeamChoiceplayer2 + fifthyour_positionplayer2
    ListPositionPlayers5TwoPlayers25()
    print("Which player do you want to pick?")
    time.sleep(1)
    fifthplayer2 = input()
    checkplayersUserplayer25()
    time.sleep(1)
    print(f"You picked {fifthplayer2} as your {fifthyour_positionplayer2}.")
    time.sleep(1)
    used_players.append(fifthplayer2)
    used_Positions2.append(fifthyour_positionplayer2)
    positionsUser2.remove(fifthyour_positionplayer2)
    time.sleep(1)
    player1Pick5()
    time.sleep(1)









#Start of game
print("Welcome to Fantasy!")
time.sleep(1)
print("How many users do you want to play with? 1, or 2?")
users = input()
if users == "1":
    print("Do you know the rules? Y/N")
    if input() == "N" or input() == "n":
        time.sleep(1)
        rulesAI()
    elif input() == "Y" or input() == "y":
        print("Great!")
        time.sleep(1)
    print("Great! Let's pick some teams!")
    time.sleep(1)
    playerPick1()
'''
elif users == "2":
    print("Do you know the rules? Y/N")
if input() == "N" or input() == "n":
    time.sleep(1)
    rulesUSERONLY()
elif input() == "Y" or input() == "y":
    print("Great! Lets play!")
    time.sleep(1)
    player1Pick1()
'''

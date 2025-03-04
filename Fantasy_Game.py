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
        ListPositionPlayers()

def checkplayersUser2():
    if player2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers2()

def checkplayersUser3():
    if player3 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player3 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers3()

def checkplayersUser4():
    if player4 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player4 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers4()

def checkplayersUser5():
    if player5 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player5 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers5()

def checkplayersUser6():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayers6()

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
    ListPositionPlayers()
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
    ListPositionPlayers2()
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
    ListPositionPlayers3()
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
    ListPositionPlayers4()
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
    ListPositionPlayers5()
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
    ListPositionPlayers6()
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
def skipTeamTwoPlayersplayer1():
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

def skipTeamTwoPlayers2():
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

def skipTeamTwoPlayers3():
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

def skipTeamTwoPlayers4():
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

def skipTeamTwoPlayers5():
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

def skipTeamTwoPlayers6():
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

def skipTeamTwoPlayersPlayer2():
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

def skipTeamTwoPlayers2Player22():
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

def skipTeamTwoPlayers3Player23():
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

def skipTeamTwoPlayers4Player24():
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

def skipTeamTwoPlayers5Player25():
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

def ListPositionPlayersTwoPlayers1():
    firstTeamAvailablePlayers = firstTeamChoiceplayer1 + firstyour_positionplayer1
    if firstTeamAvailablePlayers in globals():
        print(f"Here are the applicable players: {globals()[firstTeamAvailablePlayers]}.")

def ListPositionPlayers2TwoPlayers2():
    availablePlayers2 = randomTeamChoice2 + your_position2
    if availablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers3TwoPlayers3():
    availablePlayers3 = randomTeamChoice3 + your_position3
    if availablePlayers3 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers3]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers4TwoPlayers4():
    availablePlayers4 = randomTeamChoice4 + your_position4
    if availablePlayers4 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers4]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers5TwoPlayers5():
    availablePlayers5 = randomTeamChoice5 + your_position5
    if availablePlayers5 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers5]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers6TwoPlayers6():
    availablePlayers6 = randomTeamChoice6 + your_position6
    if availablePlayers6 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers6]}.")
        print("Which player do you want to pick?")

def ListPositionPlayersTwoPlayers21():
    firstTeamAvailablePlayers = firstTeamChoiceplayer1 + firstyour_positionplayer1
    if availablePlayers in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers]}.")

def ListPositionPlayers2TwoPlayers22():
    availablePlayers2 = randomTeamChoice2 + your_position2
    if availablePlayers2 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers2]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers3TwoPlayers23():
    availablePlayers3 = randomTeamChoice3 + your_position3
    if availablePlayers3 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers3]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers4TwoPlayers24():
    availablePlayers4 = randomTeamChoice4 + your_position4
    if availablePlayers4 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers4]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers5TwoPlayers25():
    availablePlayers5 = randomTeamChoice5 + your_position5
    if availablePlayers5 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers5]}.")
        print("Which player do you want to pick?")

def ListPositionPlayers6TwoPlayers26():
    availablePlayers6 = randomTeamChoice6 + your_position6
    if availablePlayers6 in globals():
        print(f"Here are the applicable players: {globals()[availablePlayers6]}.")
        print("Which player do you want to pick?")

def checkpositionUserPlayer1():
    if firstyour_positionplayer1 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif firstyour_positionplayer1 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer11()

def checkpositionUserPlayer12():
    if your_position2 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position2 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition2()

def checkpositionUserPlayer13():
    if your_position3 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position3 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition3()

def checkpositionUserPlayer14():
    if your_position4 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position4 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPosition4()

def checkpositionUserPlayer15():
    if your_position5 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position5 in NHLTeams.used_Positions1:
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
    if your_position not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer2()

def checkpositionUserplayer22():
    if your_position2 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position2 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer22()

def checkpositionUserplayer23():
    if your_position3 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position3 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer23()

def checkpositionUserplayer24():
    if your_position4 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position4 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer24()

def checkpositionUserplayer25():
    if your_position5 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position5 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer25()

def checkpositionUserplayer26():
    if your_position6 not in NHLTeams.used_Positions1:
        print(f"This position is available.")
        time.sleep(1)
    elif your_position6 in NHLTeams.used_Positions1:
        print("Please pick a different position. This position has been used.")
        time.sleep(1)
        redoPositionplayer26()

def checkplayersUserplayer11():
    if firstplayer not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif firstplayer in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers1()

def checkplayersUserplayer12():
    if player2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers2()

def checkplayersUserplayer13():
    if player3 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player3 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers3()

def checkplayersUserplayer14():
    if player4 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player4 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers4()

def checkplayersUserplayer15():
    if player5 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player5 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers5()

def checkplayersUserplayer16():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers6()

def checkplayersUserplayer21():
    if player not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers1()

def checkplayersUserplayer22():
    if player2 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player2 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers2()

def checkplayersUserplayer23():
    if player3 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player3 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers3()

def checkplayersUserplayer24():
    if player4 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player4 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers4()

def checkplayersUserplayer25():
    if player5 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player5 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers5()

def checkplayersUserplayer26():
    if player6 not in NHLTeams.used_players:
        print(f"This player is available.")
        time.sleep(1)
    elif player6 in NHLTeams.used_players:
        print("Please pick a different player. This player has been used.")
        time.sleep(1)
        ListPositionPlayersTwoPlayers6()

def redoPositionplayer11():
    global firstyour_positionplayer1
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer1 = input()
    checkpositionUserplayer21()

def redoPositionplayer12():
    global your_position2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position2 = input()
    checkpositionUserplayer22()

def redoPositionplayer13():
    global your_position3
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position3 = input()
    checkpositionUserplayer23()

def redoPositionplayer14():
    global your_position4
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position4 = input()
    checkpositionUserplayer24()

def redoPositionplayer15():
    global your_position5
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position5 = input()
    checkpositionUserplayer25()

def redoPositionplayer16():
    global your_position6
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position6 = input()
    checkpositionUserplayer26()

def redoPositionplayer21():
    global your_position
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position = input()
    checkpositionUserplayer21()

def redoPositionplayer22():
    global your_position2
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position2 = input()
    checkpositionUserplayer22()

def redoPositionplayer23():
    global your_position3
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position3 = input()
    checkpositionUserplayer23()

def redoPositionplayer24():
    global your_position4
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position4 = input()
    checkpositionUserplayer24()

def redoPositionplayer25():
    global your_position5
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position5 = input()
    checkpositionUserplayer25()

def redoPositionplayer26():
    global your_position6
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    your_position6 = input()
    checkpositionUserplayer26()

def player1Pick1():
    global firstTeamChoiceplayer1
    global firstyour_positionplayer1
    global firstplayer
    global firstTeamAvailablePlayers
    print("Round 1")
    time.sleep(1)
    print("I'll draw a team for you.")
    time.sleep(1)
    firstTeamChoiceplayer1 = random.choice(teams)
    print(f"The team I picked is: {firstTeamChoiceplayer1}.")
    time.sleep(1)
    skipTeamTwoPlayersplayer1()
    time.sleep(1)
    print("You pick a position.")
    time.sleep(1)
    print("Which position do you want to pick: (C, RW, LW, Def1, Def2, G) ")
    firstyour_positionplayer1 = input()
    time.sleep(1)
    checkpositionUserPlayer1()
    print(f"You picked: {firstyour_positionplayer1}.")
    time.sleep(1)
    firstTeamAvailablePlayers = firstTeamChoiceplayer1 + firstyour_positionplayer1
    ListPositionPlayersTwoPlayers1()
    print("Which player do you want to pick?")
    time.sleep(1)
    player = input()
    checkplayersUserplayer11()
    time.sleep(1)
    print(f"You picked {firstplayer} as your {firstyour_positionplayer1}.")
    time.sleep(1)
    used_players.append(firstplayer)
    used_Positions1.append(firstyour_positionplayer1)
    positionsUser1.remove(firstyour_positionplayer1)
    time.sleep(1)
    #player2Pick1()
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

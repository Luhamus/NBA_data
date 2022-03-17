from fastapi import APIRouter
import numpy as np
import pandas as pd

router = APIRouter(tags=["Get requests"])


# Making relative paths. On windows slashes would be backwards
# It is probably not a good way.
# API has to be activated from the project dir for the paths to match.
relPathTeams = "AllAboutData/Data/NBAteams.csv"
relPathPlayers = "AllAboutData/Data/Players/"



def getTeamNames():
    '''
    Returns dictionary with fetched teams' names as keys
    and full_names as values.
    '''

    teamsDf = pd.read_csv(relPathTeams).to_dict()
    team_names = {}
    for el in range(len(teamsDf["name"])):
        team_names.update({teamsDf["name"][el]: teamsDf["full_name"][el]})
    return team_names



@router.get("/teams")
def getTeams():
    '''
    Returns all the teams of NBA, converted to json,
    where each item represents one team.
    '''
    
    # Reading the data and converting into dict to send 
    teamsDf = pd.read_csv(relPathTeams).to_dict()

    teams_dict = {}
    for el in range(len(teamsDf["name"])):
        teams_dict.update({el+1 : 
                                {"Abbreviation": teamsDf["abbreviation"][el],
                                 "Name": teamsDf["name"][el],
                                 "FullName": teamsDf["full_name"][el],
                                 "City": teamsDf["city"][el],
                                 "Conference": teamsDf["conference"][el],
                                 "Division": teamsDf["division"][el]} })
    return teams_dict


@router.get("/players/{team_name}")
def getPlayers(team_name: str):
    '''
    Returns players of requested team, converted to json,
    where each item represents one player.
    '''

    teamNames = getTeamNames()
    team_name = team_name.capitalize()  #  Capitalizing in case url is given as lowercase
    if team_name in teamNames.keys():

        playersDf = pd.read_csv(relPathPlayers+teamNames[team_name]+".csv")
        playersDf = playersDf.replace({np.nan:None})  #  For Json Nan must be replaced 

        players_dict = {}
        for el in range(len(playersDf["first_name"])):
            players_dict.update({el+1 : 
                                     {"first_name": playersDf["first_name"][el],
                                      "last_name": playersDf["last_name"][el],
                                      "position": playersDf["position"][el],
                                      "height_feet": playersDf["height_feet"][el],
                                      "height_inches": playersDf["height_inches"][el]} })


        return players_dict
    else:
        return {"Error 404": "Team name Not Found"}


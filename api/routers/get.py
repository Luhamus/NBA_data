from fastapi import FastAPI, APIRouter
import numpy as np
import pandas as pd
import sys

#sys.path.append("/home/rasmus/Proge/STACC/api")
from .. import utils

router = APIRouter(tags=["Get requests"])

@router.get("/teams")
def getTeams():
    
    # Getting the data from csv files and then converting into dict to be send out on get request
    teamsDf = pd.read_csv(utils.relPathTeams).to_dict()

    teams_dict = {}
    for el in range(len(teamsDf["name"])):
        teams_dict.update({el+1 : 
                                {"Abbreviation" : teamsDf["abbreviation"][el],
                                 "Name" : teamsDf["name"][el],
                                 "FullName" : teamsDf["full_name"][el],
                                 "City" : teamsDf["city"][el],
                                 "Conference" : teamsDf["conference"][el],
                                 "Division" : teamsDf["division"][el]} })
    return teams_dict


@router.get("/players/{team_name}")
def getPlayers(team_name: str):

    teamNames = utils.getTeamNames()
    team_name = team_name.capitalize()  #  Capitalizing in case url is given as lowercase
    if team_name in teamNames.keys():

        playersDf = pd.read_csv(utils.relPathPlayers+teamNames[team_name]+".csv")
        playersDf = playersDf.replace({np.nan:None})  # For Json Nan must be replaced 

        players_dict = {}
        for el in range(len(playersDf["first_name"])):
            players_dict.update({el+1 : 
                                     {"first_name" : playersDf["first_name"][el],
                                      "last_name" : playersDf["last_name"][el],
                                      "position" : playersDf["position"][el],
                                      "height_feet" : playersDf["height_feet"][el],
                                      "height_inches" : playersDf["height_inches"][el]} })


        return players_dict
    else:
        return {"Error 404" : "Team name Not Found"}


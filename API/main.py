from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

# Making relative paths for the data, on windows slashes would have to be turned around.
# It is probably not the best way.
relPathTeams = "../AllAboutData/Data/NBAteams.csv"
relPathPlayers = "../AllAboutData/Data/Players/"

# func which return dict with team names as keys and full team names as values
def getTeamNames():
    teamsDf = pd.read_csv(relPathTeams).to_dict()
    team_names = {}
    for el in range(len(teamsDf["name"])):
        team_names.update({teamsDf["name"][el] : teamsDf["full_name"][el]})
    return team_names





@app.get("/teams")
def getTeams():
    
    # Getting the data from csv files and then converting into dict to be send out on get request
    teamsDf = pd.read_csv(relPathTeams).to_dict()

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


@app.get("/players/{team_name}")
def getPlayers(team_name: str):

    teamNames = getTeamNames()
    team_name = team_name.capitalize()  #  Capitalizing in case url is given as lowercase
    if team_name in teamNames.keys():

        playersDf = pd.read_csv(relPathPlayers+teamNames[team_name]+".csv")
        print(playersDf)
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


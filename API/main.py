from fastapi import FastAPI
import pandas as pd
import os

# Making relative paths for the data
relPathTeams = "../AllAboutData/Data/NBAteams.csv"
relPathPlayers = "../AllAboutData/Data/Players/"

app = FastAPI()

@app.get("/teams")
def teamsIntoDict():
    
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

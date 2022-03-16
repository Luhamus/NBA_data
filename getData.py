import pandas as pd
import requests
import osSpecific
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


# Delete Data Dir, if exists, and then create new. Have to do this to avoid duplicates, as Players are later appended to the files
osSpecific.deleteDataDir()
osSpecific.addDataDir()

# File variables to but data into
if osSpecific.whichOs() == "windows":
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data\Players"
else:
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data/Players"

# Requesting data about NBA teams
url = "https://free-nba.p.rapidapi.com/teams"
querystring = {"page":"0"}
headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }

# Adding data to teams file
response = requests.request("GET", url, headers=headers, params=querystring)
teamsDf = pd.DataFrame(response.json()["data"])
teamsDf.set_index("id")
teamsDf = teamsDf.drop("id", axis=1)

teamsDf.to_csv(teamsFile)

#######################################################

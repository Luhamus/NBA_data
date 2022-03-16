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
url = "https://free-nba.p.rapidapi.com/"
querystring = {"page":"0"}
headers = {
            'x-rapidapi-host': "free-nba.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
    }

# Adding data to teams file
response = requests.request("GET", url+"teams", headers=headers, params=querystring)
teamsDf = pd.DataFrame(response.json()["data"])
teamsDf.set_index("id")
teamsDf = teamsDf.drop("id", axis=1)

teamsDf.to_csv(teamsFile)

#######################################################
# Now requesting players for each team
# First request is made just to get the amount of pages that must be looped through

querystring = {"per_page":"100","page":"0"}
response = requests.request("GET", url+"players", headers=headers, params=querystring)
pageCount = response.json()["meta"]["total_pages"]


for el in range(1, pageCount+1):

    # Requesting pages in loop till pageCount
    querystring = {"per_page":"100","page":el}
    response = requests.request("GET", url+"players", headers=headers, params=querystring)
    data = response.json()["data"]
    
    for player in data:
        teamName = player["team"]["full_name"]
        playerDf = pd.DataFrame(columns=["first_name", "last_name", "position", "height_feet", "height_inches"])

        playerSeries = pd.Series({"first_name" : player["first_name"],
                                  "last_name" : player["last_name"],
                                  "position" : player["position"],
                                  "height_feet" : player["height_feet"],
                                  "height_inches" : player["height_inches"]})

        #add player to dataframe
        playerDf.loc[len(playerDf)] = playerSeries 
        #add dataframe to File
        playerDf.to_csv(playersDir+teamName, mode='a', index=False, header=False)
    print("Page "+el+" read.") 
print("All done, check Data Dir")
    






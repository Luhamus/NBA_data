import pandas as pd
import requests
from utils import osSpecific  #  Some functions to delete and create directoryes needed for data storing
from dotenv import load_dotenv
import os

'''
This python script fetches NBA teams and its players (currently playing and retired) and some
additional information about them. 
The data is stored in the current working directory (any existing "Data" file is overwritten.
Data is in csv format.

Author: Rasmus Luha
Created_at: 16.03.2022
Data fetched from: https://rapidapi.com/theapiguy/api/free-nba/
'''

# Loading API key from environment variables.
load_dotenv()
API_KEY = os.getenv("API_KEY")

# To use this script, you should make .env file in current dir and add there: API_KEY = your API_key
# You can get the API key from url listed above.

# API request details
url = "https://free-nba.p.rapidapi.com/"
headers = {
            'x-rapidapi-host': "free-nba.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
          }

# File name variables to store data in 
if osSpecific.whichOs() == "windows":
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data\Players\\"
else:
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data/Players/"

# Create new Data directory in order to avoid duplicates, when data is requested multiple times 
osSpecific.deleteDataDir()
osSpecific.addDataDir()



###### Functions ######

def getTeamsData(url, headers):

    querystring = {"page":"0"}
    response = requests.request("GET", url+"teams", headers=headers, params=querystring)

    teamsDf = pd.DataFrame(response.json()["data"])
    teamsDf.set_index("id")
    teamsDf = teamsDf.drop("id", axis=1)
    teamsDf.to_csv(teamsFile)
    print("Teams data stored in Data directory as \"NBAteams.csv\"")


def getPlayerData(url, headers):

    print("Stared reading players data")

    # First request is made just to get the amount of pages that must be looped through
    querystring = {"per_page":"100","page":"0"}
    response = requests.request("GET", url+"players", headers=headers, params=querystring)
    pageCount = response.json()["meta"]["total_pages"]
    
    print("Pages to read: "+str(pageCount)) 
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
            playerDf.to_csv(playersDir+teamName+".csv", mode='a', index=False, header=False)
    
        print("Page "+str(el)+" read.") 
    print("All done, check \"Data\" Dir.")




# Requesting and storing data
if __name__ == "__main__":
    getTeamsData(url, headers)
    getPlayerData(url, headers)

'''NBA data reciever

This python script fetches NBA teams and its players (including retired)
with some additional information about them. 
The data is stored in the current working directory and thus, 
any existing "Data" file is overwritten. Data will be in csv format.

To use this script, "pandas" and "python-dotenv" must be installed
You also have to make .env file in current dir and add there: API_KEY = your API_key
You can get the API key from url below.

Used API: https://rapidapi.com/theapiguy/api/free-nba/
'''

import os
import utils #  Some functions to delete and create directories for data
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

# API request details
url = "https://free-nba.p.rapidapi.com/"
headers = {
            "x-rapidapi-host": "free-nba.p.rapidapi.com",
            "x-rapidapi-key": API_KEY
          }


# Createing file name variables to store data in 
if utils.whichOs() == "windows":
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data\Players\\"
else:
    teamsFile = "Data/NBAteams.csv"
    playersDir = "Data/Players/"


###### Functions ######

def getTeamsData(url, headers):
    '''Requests Data about NBA teams and stores it.
    Takes API url as first and its headers as second argument.'''

    querystring = {"page": "0"}
    response = requests.request("GET", url+"teams", headers=headers, params=querystring)

    #If API_KEY doesn't match, or other error, then stop function
    if response.status_code != 200:
        print("Failed to fetch from API: response code: " + str(response.status_code))
        print(response.text)
        return

    teamsDf = pd.DataFrame(response.json()["data"])
    teamsDf.set_index("id")
    teamsDf = teamsDf.drop("id", axis=1)

    # Creating new Data dir to avoid duplicates (due appending)
    utils.deleteDataDir()
    utils.addDataDir()

    teamsDf.to_csv(teamsFile)
    print("Teams data stored in Data directory as \"NBAteams.csv\"")


def getPlayerData(url, headers):
    '''Requests Data about NBA players and stores it, based on teams
    Takes API url as first and its headers as second argument.'''

    # First request is made to get the page count to loop
    querystring = {"per_page": "100","page":"0"}
    response = requests.request("GET", url+"players", headers=headers, params=querystring)

    #If API_KEY doesn't match, or other error, then stop function
    if response.status_code != 200:
        return

    pageCount = response.json()["meta"]["total_pages"]  #  Got the page count here

    print("Stared reading players data")
    print("Pages to read: "+str(pageCount)) 
    for el in range(1, pageCount+1):
    
        # Requesting pages in loop till pageCount is reached
        querystring = {"per_page": "100","page": el}
        response = requests.request("GET", url+"players", headers=headers, params=querystring)
        data = response.json()["data"]
        
        # Making dataframe for each player to store it suitable file
        for player in data:
            teamName = player["team"]["full_name"]
            playerDf = pd.DataFrame(columns=["first_name", "last_name",
                                             "position", "height_feet", 
                                             "height_inches"])
    
            playerSeries = pd.Series({"first_name": player["first_name"],
                                      "last_name": player["last_name"],
                                      "position": player["position"],
                                      "height_feet": player["height_feet"],
                                      "height_inches": player["height_inches"]})
    
            
            playerDf.loc[len(playerDf)] = playerSeries 

            # Add dataframe to File, if first to be added, then also add column names
            hdr = False if os.path.isfile(playersDir+teamName+".csv") else True
            playerDf.to_csv(playersDir+teamName+".csv", mode='a', index=False, header=hdr)
    
        print("Page "+str(el)+" read.") 
    print("All done, check \"Data\" Dir.")



if __name__ == "__main__":


    getTeamsData(url, headers)
    getPlayerData(url, headers)


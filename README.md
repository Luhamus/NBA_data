# Overview
This project has the functionality to fetch data about NBA and store it in csv format files.
It also has an API to serve the data. API can be accessed here.

## How to use
### API
From the api you can fetch data as follows:
* For teams, the endpoint is "/teams" and you can fetch data as follows:
'''bash
  https//:{api_url}/teams
'''
* For player information, the endpoint is "/players/{team_name}
 - you can get the team name from fetching the teams data.
 - Examples: Bulls, Celtics, Hawks, Nets, Hornets.
 '''
    https//:{api_url}/players/celtics
    https//:{api_url}/players/hawks
 '''
 - NB: you shouldn't use the "full_name", like "Chicago Bulls".


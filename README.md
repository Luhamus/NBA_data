# Overview
This project has the functionality to fetch data about NBA and store it in csv format files.
It also has an API to serve the data.
API is at this [url](https://luhamus-nba-data.herokuapp.com/).

## How to use
### API
From the api you can fetch data as follows:
* For teams, the endpoint is "/teams" and you can fetch data as follows:
```
{api_url}/teams
```
or just use [this](https://luhamus-nba-data.herokuapp.com/teams).

* For player information, the endpoint is "/players/{team_name}
 - you can get the team name from fetching the teams data.
 '''
    {api_url}/players/{team_name}
 '''
 - Examples with Bulls, Celtics, Hawks:
 * [https://luhamus-nba-data.herokuapp.com/teams/bulls](https://luhamus-nba-data.herokuapp.com/teams/bulls).
 * [https://luhamus-nba-data.herokuapp.com/teams/celtics](https://luhamus-nba-data.herokuapp.com/teams/celtics).
 * [https://luhamus-nba-data.herokuapp.com/teams/hawks](https://luhamus-nba-data.herokuapp.com/teams/hawks).
 - NB: you shouldn't use the "full_name", like "Chicago Bulls".

### Fetching Data
Code for fetching data in in directory AllAboutData, where the 
fetched data will also be stored.
To use the data fetching script, you should clone the repo and do following:
```bash
cd {cloned_repo_name}
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then you should make a file 
```
.env
```
and add your api key there like this.
```bash
API_KEY = {your_api_key}
```
You can get yourself the api key from this [link](https://rapidapi.com/theapiguy/api/free-nba/).
You have to subscribe to the API, but it is free. Once you have done that you can use the script.
```bash
cd AllAboutData
python getData.py
```

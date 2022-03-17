# Overview
This project has the functionality to fetch data about NBA and store it in csv format files.
It also has an API to serve the data.
API is at this [https://luhamus-nba-data.herokuapp.com/](https://luhamus-nba-data.herokuapp.com/).

# How to use
## API
You can fetch the data from API as follows:
* For teams, the endpoint is "/teams" and you can fetch like that:
```
{api_url}/teams
```
  or just use [this](https://luhamus-nba-data.herokuapp.com/teams) link.

<br>
<br>
 * For players information, you can search by the team. the endpoint is "/players/{team_name}
 * you can get the team name from fetching the teams data from /teams.
 * Examples with Bulls, Celtics, Hawks:
 * [https://luhamus-nba-data.herokuapp.com/players/bulls](https://luhamus-nba-data.herokuapp.com/players/bulls).
 * [https://luhamus-nba-data.herokuapp.com/players/celtics](https://luhamus-nba-data.herokuapp.com/players/celtics).
 * [https://luhamus-nba-data.herokuapp.com/players/hawks](https://luhamus-nba-data.herokuapp.com/players/hawks).
 > :warning: You shouldn't use the "fullName", like "Chicago Bulls".

### API on localhost
To run the API locally, you should first clone the Repo and do the following:
```bash
cd {cloned_repo_name}
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
then you can run the API on localhost, at port 8000, as follows:
```
uvicorn api.main:app --reload
```
where reload option is for development.
> :warning: When you are running API locally, you should first fetch the Data to be served.
> For that, read the next section


## Fetching Data
Code for fetching data in in directory AllAboutData, where the 
fetched data will also be stored.
To use the data fetching script, you should follow the same steps as
for [running API locally](#api-on-localhost). Then you should make a file 
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

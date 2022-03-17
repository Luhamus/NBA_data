import pandas as pd

# Making relative paths. On windows slashes would be backwards
# It is probably not the best way.
relPathTeams = "../AllAboutData/Data/NBAteams.csv"
relPathPlayers = "../AllAboutData/Data/Players/"

def getTeamNames():
    '''
    Returns dictionary with fetched teams' names as keys
    and full_names as values.
    '''

    teamsDf = pd.read_csv(relPathTeams).to_dict()
    team_names = {}
    for el in range(len(teamsDf["name"])):
        team_names.update({teamsDf["name"][el] : teamsDf["full_name"][el]})
    return team_names

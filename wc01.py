import numpy as np
import pandas as pd
import random

# class that contains the teamname, rating and laungauge 
class crtp :
    def __init__(self, team_name, rate, language = ''): #, OMW, time, score):
        self.team_name = team_name
        rating = []
        rating.append(rate)
        self.rating = rating
        #self.OMW = OMW
        #self.time = time
        self.language = language
        #self.score = score




# list of players
list_of_teamnames = [ 'A01',
                    'A02',
                    'A03',
                    'A04',
                    'A05',
                    'A06',
                    'A07',
                    'A08',
                    'A09',
                    'A10',
                    'A11',
                    'A12',
                    'A13',
                    'A14',
                    'A15',
                    'A16',
                    'A17',
                    'A18',
                    'A19',
                    'A20',
                    'A21',
                    'A22',
                    'A23',
                    'A24',
                    'A25',
                    'A26',
                    'A27',
                    'A28',
                    'A29',
                    'A30',
                    'A31',
                    'A32',
                    'A33',
                    'A34',
                    'A35',
                    'A36',
                    'A37',
                    'A38',
                    'A39',
                    'A40',
                    'A41',
                    'A42',
                    'A43',
                    'A44',
                    'A45',
                    'A46',
                    'A47',
                    'A48',
                    'A49',
                    'A50',
                    ]


list_of_ratings = [
                    77,
                    60,
                    83,
                    84,
                    71,
                    66,
                    70,
                    82,
                    80,
                    77,
                    67,
                    89,
                    77,
                    66,
                    81,
                    92,
                    89,
                    79,
                    69,
                    93,
                    75,
                    97,
                    86,
                    92,
                    96,
                    89,
                    75,
                    96,
                    96,
                    62,
                    93,
                    92,
                    70,
                    62,
                    60,
                    72,
                    79,
                    74,
                    93,
                    81,
                    89,
                    85,
                    94,
                    69,
                    92,
                    65,
                    88,
                    93,
                    99,
                    62,
                    ]



list_of_languages = [ 
                    'C++',
                    'P',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'C++',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'C++',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'P',
                    'C++',
                    'P',
                    'P',
                    'P',
                    ]

#print(len(list_of_teamnames), " ", len(list_of_ratings), " ", len(list_of_languages))

# a list of class crtp that contains all the teams
list_of_teams = []

for i in range (0, 50) :
    objx = crtp(list_of_teamnames[i], list_of_ratings[i], list_of_languages[i]) #, 0, 0, 0)
    list_of_teams.append(objx)



# a dataframe that contains all the stats -> team(Player), matches played, points, oppenent match Win rate (OMW), average time (TIME_AV)
standings_df = pd.DataFrame(list(zip(list_of_teams, 
                                     [0 for i in range(0, 50)],
                                     [0 for i in range(0, 50)],
                                     [0 for i in range(0, 50)], 
                                     [0 for i in range(0, 50)])),
                                    columns = ["Player", "Played", "Points", "OMW", "TIME_AV"])


"""
The average time is defined as follows :-
    if the team wins, the faster it wins, the better, thus we take its -ve value (higher magnitude, lower value)
    if the team loses, the slower it loses, the better, thus we take its +ve value 
    for a bye, for the sake of simplicity, we take match time = 0 (as there was no match, so no time taken)

"""


# a dictionary that contains the record of all the matches
match_history = {}


def update_standings(match_history,
                     list_of_teams):
    """
    Generates the standings of a given match history dictionary.
    
    Requires match_history plus the list of remaining players (in case of drops)
        Also because its easier.
    
    The returned standings_df has the following:
        "Player", "Points", "OMW", "TIME_AV"

    """
    
    # We have an opponents key, but we'll get rid of it after calculating OMW
    standings_dict = {
        "Player": list_of_teams,
        "Played": [],
        "Points": [],
        # Add lists for Opponent Match Win%, TIME_AV and Opponents
        "OMW": [],
        "TIME_AV":[],
        "Opponents": []
    }
    
    # For each player 
    for player in list_of_teams:
        
        played = 0
        points = 0
        # Create a list that will house the opponents they've played.
        opponents = []

        # a list that contains the match timings
        time_for_matches = []
        
        # Check to see if they were involved in a match
        for match in match_history:
            # If they were player 1
            if player == match_history[match]["Player_1"]:
                # Increased played by 1
                played += 1

                # Fill the opponents list with the names of each opponent

                # if there is not a bye
                if match_history[match]["Player_1"] != match_history[match]["Player_2"] :
                    opponents.append(match_history[match]["Player_2"])
                
                # fill the time of matches
                time_for_matches.append(-match_history[match]["Time_match"])
                points += 1
                
            
            # If they were player 2
            elif player == match_history[match]["Player_2"]:
                
                # Increase games played and add opponent if there is not a bye
                if match_history[match]["Player_1"] != match_history[match]["Player_2"] :
                    played += 1
                    opponents.append(match_history[match]["Player_1"])
                    time_for_matches.append(match_history[match]["Time_match"])

        # taking the average of total time 
        time_agr = 0  
        if len(time_for_matches)> 0:
            time_agr = np.round(np.mean(time_for_matches), 3)
        
                
                    
        # Once we've looped through all the matches
        # Append the stats to the standings_dict
        standings_dict["Played"].append(played)
        standings_dict["Points"].append(points)
        standings_dict["Opponents"].append(opponents)
        standings_dict["TIME_AV"].append(time_agr)
                
    
    # We can only calculate OMW after all matches have been added to the standings
    for opponent_list in standings_dict["Opponents"]:
        
        # Create a list with the OMW of each of their opponents.
        running_omw = []
        
        # For each opponent they've previously played, find their win percentage.
        for opponent in opponent_list:
            
            # Find index of their opponent
            opponent_index = standings_dict["Player"].index(opponent)

            # Calculate their OMW by dividing the points they've earned by the 
            # number of games they've played.
            running_omw.append(standings_dict["Points"][opponent_index] / 
                               standings_dict["Played"][opponent_index])

        # If it's the first round, no one has played anyone yet and the length of running_omw 
        # will be 0. 
        if len(running_omw) == 0:
            standings_dict["OMW"].append(0)
        else:
            # Get the average OMW and round to three decimal places. 
            standings_dict["OMW"].append(np.round(np.mean(running_omw), 3))
            player.OMW = np.round(np.mean(running_omw), 3)

        #standings_dict["TIME_AV"].append(player.time)
    
    # Remove the opponents key:value pair
    standings_dict.pop("Opponents")
    
    # Turn the dictionary into a dataframe
    standings_df = pd.DataFrame.from_dict(standings_dict).sort_values(["Points", "OMW", "TIME_AV"], ascending = False)

    #print(standings_df)
    
    return standings_df







def add_result(match_num, player_one, player_two, match_history):
    """
    Prompts user for result and records it in the given dictionary
    
    Arguments:
    
        match_num - int
        player_one - class
        player_two - class
        
    
    match_history - the dictionary where we want to store this data.
    
    Does not return anything, merely updates the match_history dictionary with the
    results

    We also update the ratings, but as there is no pass by refernce for integers in python, 
    we have used ratings as a list so that it can be passed byrefernce
    """

    # if there is a bye
    if player_one == player_two :
        match_history[match_num] = {
                'Player_1': player_one,
                'Player_2': player_two,
                'Time_match' : 0
            }
        return
    
    # ratings of players passed by refernce
    rating01 = player_one.rating[0] 
    rating02 = player_two.rating[0]

    # time ggenerated as a random int between 5 and 10
    time01 = random.randint(5, 10)

    # noise generated randomly between -4 and 4 for ratings
    noise01 = random.randint(-4, 4)
    noise02 = random.randint(-4, 4)

    rating01 += noise01
    rating02 += noise02

    # difference of ratings, converted to absolute value
    diff01 = rating01 - rating02

    if diff01<0 :
        diff01 = -diff01

    """
    Below, we do the following,
    1) apply the condition of difference in rating 
    2) calculate the probabilty of the higher rated player winning
    3) pass the winner as player 1 and loser as player 2 with time in match history

    """


    # applying condition 1
    if diff01<5 : 
        prob01 = random.randint(0,1)
        if prob01<1 :
            if rating01>rating02 :
                player_one.rating[0] += 2
                player_two.rating[0] -= 2

                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }
            elif rating01<rating02:
                player_one.rating[0] += -2
                player_two.rating[0] -= -2
                    
                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += 3
                player_two.rating[0] -= 3
                    
                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }

        
        else:
            if rating01>rating02 :
                player_one.rating[0] += -5
                player_two.rating[0] -= -5

                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }
            elif rating01<rating02:
                player_one.rating[0] += 5
                player_two.rating[0] -= 5
                    
                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += -3
                player_two.rating[0] -= -3
                    
                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }


    # applying condition 2
    elif diff01>4 and diff01<11 :
        prob03 = random.randint(1, 100)
        if prob03<66 :
            if rating01>rating02 :
                player_one.rating[0] += 2
                player_two.rating[0] -= 2

                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += -2
                player_two.rating[0] -= -2
                    
                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }

        else:
            if rating01>rating02 :
                player_one.rating[0] += -5
                player_two.rating[0] -= -5

                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += 5
                player_two.rating[0] -= 5
                    
                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }
            
        

    # applying condition 3
    else:
        prob04 = random.randint(1, 10)
        if prob04<2 :
            if rating01>rating02 :
                player_one.rating[0] += 2
                player_two.rating[0] -= 2

                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += -2
                player_two.rating[0] -= -2
                    
                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }

        else:
            if rating01>rating02 :
                player_one.rating[0] += -5
                player_two.rating[0] -= -5

                match_history[match_num] = {
                    'Player_1': player_two,
                    'Player_2': player_one,
                    'Time_match' : time01
                }
            else:
                player_one.rating[0] += 5
                player_two.rating[0] -= 5
                    
                match_history[match_num] = {
                    'Player_1': player_one,
                    'Player_2': player_two,
                    'Time_match' : time01
                }

    







def determine_pairings(standings_df, match_history):
    """
    Determines pairings for a set of standings and the match_history of the tournament
    
    standings_df should have:
        "Player", "Points", "OMW", "TIME_AV"
    """
    # Create a list to hold our pairings
    pairings = list()


    
    # Sort the standings_df from best performing to worst performing
    # Note that we use sample(frac = 1) to ensure that the duplicates are not sorted
    # alphabetically
    sorted_df = standings_df.sample(frac = 1).sort_values(["Points", "OMW"], ascending = False)

    
    # Note that this preserves the ordering
    player_list = list(sorted_df["Player"].unique())

    # prepare two seperate lists for language C++ and Python
    player_list_C = list()
    player_list_P = list()

    for i in range(0,50) :
        if player_list[i].language == 'C++' :
            player_list_C.append(player_list[i])
        else :
            player_list_P.append(player_list[i])

    # a list of player that were previously appointed a bye
    prev_byed = list()

    for match in match_history:
        
        # If our primary player was one of the belligerents, put the other guy in
        # previously played
        if match_history[match]["Player_2"] == match_history[match]["Player_1"]:
            prev_byed.append(match_history[match]["Player_2"])
        
    # determine a player randomly which is not byed before in C++
    while len(player_list_C) == 13 :


        xx01 = random.randint(0,12)

        teamxx01 = player_list_C[xx01]
        damn = True

        for teamoh in prev_byed :
            if teamoh == teamxx01 :
                damn =False

        if damn == True : 
            pairings.append([player_list_C[xx01], player_list_C.pop(xx01)])
            
    # determine a player randomly which is not byed before in Python
    while len(player_list_P) == 37 :
        xx02 = random.randint(0,36)
        

        teamxx02 = player_list_P[xx02]
        damn = True

        for teamoh in prev_byed :
            if teamoh == teamxx02 :
                damn =False

        if damn == True : 
            pairings.append([player_list_P[xx02], player_list_P.pop(xx02)])
            
    
    
    # Code runs until player_list is empty in C++, i.e. there are no players left to be paired
    while len(player_list_C) > 0:
        
        # We are going to try and match the first player in player_list_C - the "primary"
        # player. They'll be denoted by player_list_C[0]
        
        # First check - who has this player played before?
        previously_played_0 = []
        
        for match in match_history:

            #print( match_history[match]["Player_1"].team_name,  match_history[match]["Player_2"].team_name)

            # if there was a bye, continue
            if match_history[match]["Player_2"] == match_history[match]["Player_1"]:
                continue
        
            # If our primary player was one of the belligerents, put the other guy in
            # previously played
            if player_list_C[0] == match_history[match]["Player_1"]:
                previously_played_0.append(match_history[match]["Player_2"])
            elif player_list_C[0] == match_history[match]["Player_2"]:
                previously_played_0.append(match_history[match]["Player_1"])
                
        # a boolean value that checks if all the current players have been not matched with 1st player - player_list_C[0]
        yep01 = True

        # Pair with next highest legal player. 
        for index in range(1, len(player_list_C)):
            # If the players have not played before, add them to pairings and remove them
            # from the player_list
            # Then break the for loop.
            if player_list_C[index] not in previously_played_0:
                # Note that we have to use .pop(index-1) because
                # .pop(0) happens FIRST, so all indices are moved back by 1.
                pairings.append([player_list_C.pop(0), player_list_C.pop(index-1)])
                yep01 == False
                break
        
        # if the loop was not broken, match the first 2 opponents
        if yep01 == True and len(player_list_C)>0:
            pairings.append([player_list_C.pop(0), player_list_C.pop(0)])
    
    



# Code runs until player_list_P is empty, i.e. there are no players left to be paired
    while len(player_list_P) > 0:
        
        # We are going to try and match the first player in player_list - the "primary"
        # player. They'll be denoted by player_list[0]
        
        # First check - who has this player played before?
        previously_played_1 = []
        
        for match in match_history:

            if match_history[match]["Player_2"] == match_history[match]["Player_1"]:
               continue
        
            # If our primary player was one of the belligerents, put the other guy in
            # previously played
            if player_list_P[0] == match_history[match]["Player_1"]:
                previously_played_1.append(match_history[match]["Player_2"])
            elif player_list_P[0] == match_history[match]["Player_2"]:
                previously_played_1.append(match_history[match]["Player_1"])
                
        # a boolean value that checks if all the current players have been not matched with 1st player - player_list_P[0]
        yep02 = True

        # Pair with next highest legal player. 
        for index in range(1, len(player_list_P)):
            # If the players have not played before, add them to pairings and remove them
            # from the player_list
            # Then break the for loop.
            if player_list_P[index] not in previously_played_1:
                # Note that we have to use .pop(index-1) because
                # .pop(0) happens FIRST, so all indices are moved back by 1.
                pairings.append([player_list_P.pop(0), player_list_P.pop(index-1)])
                yep02 =False
                break

        # if the loop was not broken, match the first 2 opponents
        if yep02 == True and len(player_list_P)>0:
            pairings.append([player_list_P.pop(0), player_list_P.pop(0)])
    
    # Return our list of pairings
    return pairings







def display_leaderboard(standings_df):
    """
    Displays the leaderboard in a tabular format.
    
    Arguments:
    standings_df -- DataFrame containing player standings with columns: "Player", "Points", and "OMW"
    """
    print("\nLeaderboard:")
    print("{:<10} {:<10} {:<10} {:<10}".format("Player", "Points", "OMW", "TEAM_AV"))
    for index, row in standings_df.iterrows():
        print("{:<10} {:<10} {:<10} {:<10}".format(row['Player'].team_name, row['Points'], row['OMW'], row["TIME_AV"]))





def conduct_matches(pairings, match_history):
    """
    Conducts matches based on the pairings and updates the match history.
    
    Arguments:
    pairings -- List of pairs of players to play against each other
    match_history -- Dictionary representing the history of matches
    
    Returns:
    Updated match_history dictionary
    """
    for idx, pairing in enumerate(pairings):
        player_one, player_two = pairing
        
        
        # Add the result to the match history
        add_result(len(match_history), player_one, player_two, match_history)
    
    return match_history





"""
Our main loop that runs 10 times for 10 rounds,
determining the pairings and conducting matches,
while updating the standings.
It prints the leaderboard after every round.

"""

for i in range (0, 10) :

    pairingss = determine_pairings(standings_df, match_history)

    match_history = conduct_matches(pairingss, match_history)

    standings_df = update_standings(match_history, list_of_teams)

    print()
    print( "ROUND" ,i+1)
   
    display_leaderboard(standings_df)

    

print()
        

    




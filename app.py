import constants

global exp_players
exp_players = []

global non_exp_players
non_exp_players = []

global new_list
new_list = []

panthers = []
bandits = []
warriors = []

def clean_players(dict_list):
    dict_list = dict_list.copy()
    val_list = []
    for item in dict_list:
        for val in item:
            val_list.append(item[val])
        new_list.append(val_list)
        val_list = []
    return new_list


def clean_guardians(team):
    team = team.copy()
    for i in team:
        if i[1].find("and") >= 0:
            name = i.pop(1)
            name = name.split(" and ")
            i.insert(1, name)
    return team
    
    
def to_boolean(players_list):
    for player in players_list:
        if player[2].lower() == 'yes':
            player[2] = True
        else:
            player[2] = False

        
def remove_inches(players_list):
    for player in players_list:
        player[3] = int(player[3][0:2])
    

def clean_data(players_list):
    clean_players(constants.PLAYERS)    
    clean_guardians(players_list)
    to_boolean(players_list)
    remove_inches(players_list)
    

def exp_vs_non_exp(players_list):
    for player in players_list:
        if player[2] == True:
            exp_players.append(player)
        else:
            non_exp_players.append(player)
    return exp_players
    return non_exp_players


def balance_teams(exp_players, non_exp_players, team1, team2, team3):
    for player in exp_players:
        if len(team1) == len(exp_players) / len(constants.TEAMS):
            if len(team2) == len(exp_players) / len(constants.TEAMS):
                team3.append(player)
            else:
                team2.append(player)
        else:
            team1.append(player)
    
    for player in non_exp_players:
        if len(team1) == len(non_exp_players) / len(constants.TEAMS) + len(exp_players) / len(constants.TEAMS):
            if len(team2) == len(non_exp_players) / len(constants.TEAMS) + len(exp_players) / len(constants.TEAMS):
                team3.append(player)
            else:
                team2.append(player)
        else:
            team1.append(player)
    return team1
    return team2
    return team3
        
        
def display_players(team):
    player_names = []
    for i in team:
        player_names.append(i[0])
    names_str = ", "
    return names_str.join(player_names)
        
        
def display_guardians(team):
    guardian_names = []
    for player in team:
        if len(player[1]) <= 2:
            guardians = player[1]
            for i in guardians:
                guardian_names.append(i)
        else:
            guardian_names.append(player[1])

    names_str = ", "
    
    return names_str.join(guardian_names)


def calc_avg_height(team):
    total_height = 0
    for i in team:
        height = i[3]
        total_height += height
    avg_height = total_height / len(team)
    return round(avg_height, 1)
    
    
def display_team(team):
    print("Total players: {}".format(len(team)))
    print("Number of experienced players: {}".format(int(len(exp_players) / len(constants.TEAMS))))
    print("Number of inexperienced players: {}".format(int(len(non_exp_players) / len(constants.TEAMS))))
    print("Average height: {}".format(calc_avg_height(team)))
    print("Players on the team\n    {}".format(display_players(team)))
    print("Guardians of the team\n    {}".format(display_guardians(team)))

if __name__ == '__main__':
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    
    clean_data(new_list)
    
    exp_vs_non_exp(new_list)
    
    balance_teams(exp_players, non_exp_players, panthers, bandits, warriors)
    
    print("BASKET TEAM STATS TOOL: JR EDITION\n")
    
    while True:
        print("-----MENU-----\n")
        print("You have two choices:\n1) Display Team Stats\n2) Quit\n")
        choice = input("Enter an option: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > 2:
                raise ValueError("Oops! Looks like you entered a number other than 1 or 2")
        except ValueError as err:
            print("{}".format(err))
            print("Please try again.\n")
        else: 
            print()
            if choice == 2:
                break
            else:
                while True:
                    print("1) Panthers\n2) Bandits\n3) Warriors\n")
                    team = input("Pick a team by the number: ")
                    try:
                        team = int(team)
                        if team < 1 or team > len(constants.TEAMS):
                            raise ValueError("Oops! Looks like you entered a number outside the range of 1 to {}".format(len(constants.TEAMS)))
                    except ValueError as err:
                        print("{}".format(err))
                        print("Please try again.\n")
                    else:
                        if team == 1:
                            print("Team: Panthers Stats\n------------")
                            display_team(panthers)
                            print()
                        elif team == 2:
                            print("Team: Bandits Stats\n------------")
                            display_team(bandits)
                            print()
                        elif team == 3:
                            print("Team: Warriors Stats\n------------")
                            display_team(warriors)
                            print()
                        repeat = input("Press ENTER to continue...")
                        print()
                        break
            

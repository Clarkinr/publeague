# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def name_league():
    print("Welcome to the publeague tournament tracker!\n")
    tour_name = input("What is the name of your tournament\n")
    return tour_name
name_league()
print(tour_name)

def tournament_size():
    num_teams = int(input("Please enter the number of teams in your torunament: \n"))
    print(f"Your tournament bracket will contain {num_teams} teams\n")
    return num_teams
tournament_size()


def tour_typ():
    print("Please select a tournament type:\n 1. Round Robin\n 2. Round Robin Double Split\n 3. Single Elimination\n 4. Double Elimination\n")
    tour_typ = input("Type number for option 1, 2, 3 or 4 : \n")

def create_team_names(tournament_size):
    team_names = []
    for i in range(0,num_teams):
        team = str(input())

        team_names.append(team)
    print(team_names)
create_team_names()


def generate_single_elim(self, num_teams, tour_typ, team_names):
    self.num_teams = num_teams
    self.tour_typ = tour_typ
    self.team_names = [team_names]

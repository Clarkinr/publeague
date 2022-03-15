# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tournament_tracker')

def new_tournament():
    """
    Creates a new spreadsheet which will contain team and game information
    """
    print("What is the name of this torunament\n")
    tour_name = input("Tournament Name: \n")
    print(f'Your tournament has been named {tour_name}\n')

new_tournament()

def tour_size():
    """
    Requests tournament size and type from the user and generates the bracket
    """
    num_teams = [4,8,16]
    input_num_teams = int(input("Enter the number of teams in the tournament (4/8/16): \n"))
    if input_num_teams in num_teams:
        print(f"Your tournament will contain {input_num_teams} teams\n")
    else:
        print("Tournament size must be 4,8 or 16\n Please enter a valid number\n")
        tour_size()

tour_size()

def tour_typ():
    print("Choose type of torunament to create\n")
    print("Your options are \n1. Single Elimination \n2. Double Elimination \n3. Round Robin \n4. Round Robin Split")
    tour_select = int(input("Enter the number of the type of torunament you would like to run\n"))
    if tour_select == 1:
        print("You have chosen Single Elimination\n")
    elif tour_select == 2:
        print("You have chosen Double Elimination\n")
    elif tour_select == 3:
        print("You have chosen Round Robin\n")
    elif tour_select == 4:
        print("You have chosen Round Robin Split\n")
    else: 
        print("You must enter a single number 1,2,3 or 4\n please try again\n")
        tour_typ()    
tour_typ()

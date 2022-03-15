# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    num_teams = input("Enter the number of teams taking part in the tournament: \n")
    
tour_size()
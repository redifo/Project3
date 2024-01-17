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
SHEET = GSPREAD_CLIENT.open('project3-ci')

#sheet with 2309 5 letter words
answers_sheet = SHEET.worksheet('answer')
#sheet with 14885 5 letter words
words_sheet = SHEET.worksheet('words')

all_answers = answers_sheet.get_all_values()
all_words = words_sheet.get_all_values()

print(all_answers[1])
print(all_words[1])

def print_menu():
    print("\n" * 2)  
    print("""
            __        __                     _   _        
            \ \      / /   ___    _ __    __| | | |   ___ 
             \ \ /\ / /   / _ \  | '__|  / _` | | |  / _ \.
              \ V  V /   | (_) | | |    | (_| | | | |  __/
               \_/\_/     \___/  |_|     \__,_| |_|  \___|
""")
    print("-" * 80) 
    print("1. Start Game")
    print("2. View High Scores")
    print("3. Exit")
    print("-" * 80)
    print("Select an option: ", end="")

print_menu()
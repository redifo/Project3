# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3-ci')


class WordleGame:
    def __init__(self, sheet):
        #sheet with 14885 5 letter words
        self.answers_sheet = sheet.worksheet('answer')
        #sheet with 2309 5 letter words
        self.words_sheet = sheet.worksheet('words')
        self.all_answers = self.answers_sheet.get_all_values()
        self.all_words = self.words_sheet.get_all_values()
        self.player_name = None

    def start_game(self):
        self.player_name = self.get_player_name()
        print(f"Hello, {self.player_name}!")

        

    def get_player_name(self):
        while True:
            name = input("Please enter your name: ")
            if len(name) > 2:
                return name.capitalize()
            else:
                print("Your name must be at least 3 characters long. Please try again.")
                
    def how_to_play(self):
        print("How to Play Wordle:")
        print("1. You will be asked to enter your name. Once your name is entered, the game will begin")
        print("2. You'll be asked to guess a 5-letter word. The game will provide feedback on your guess attempt.")
        print("3. The feedback consists of two elements: correct letters in the correct position and correct letters in the wrong position (*)")
        print("4. For example, if the secret word is 'APPLE' and you guess is 'ADOPT' the feedback might look like this:")
        print("   A _ _ P*_ 1as you can see the 'A' is in correct position with no marking and P is with an asterix idicating the letter is present in the word but in a different location")
        print("5. If you correctly guess the word within the specified number of attempts, you win the game!")
        print("6. You can choose to exit the game at any time")
        print("7. Have fun!")


def print_menu():
    """
    Function to display the main menu options and the ascii wordle title.
    Calls the corresponding functions for each option
    """
    print("\n" * 1)  
    print("""
            __        __                     _   _        
            \ \      / /   ___    _ __    __| | | |   ___ 
             \ \ /\ / /   / _ \  | '__|  / _` | | |  / _ \.
              \ V  V /   | (_) | | |    | (_| | | | |  __/
               \_/\_/     \___/  |_|     \__,_| |_|  \___|
""")
    print("-" * 80) 
    print("1. Start Game")
    print("2. Select difficulty")
    print("3. How to play")
    print("-" * 80)
    menu_choice= input("Select an option: ")
    return menu_choice
     


def main():
    while True:
        choice = print_menu()
        #create an instance of the WordleGame class named game
        game = WordleGame(SHEET)

        if choice == "1":
            game.start_game()
        elif choice == "2":
            print("d")
            
        elif choice == "3":
            game.how_to_play()
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
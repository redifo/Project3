
import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3-ci')

title="""
             __        __                     _   _        
             \ \      / /   ___    _ __    __| | | |   ___ 
              \ \ /\ / /   / _ \  | '__|  / _` | | |  / _ \.
               \ V  V /   | (_) | | |    | (_| | | | |  __/
                \_/\_/     \___/  |_|     \__,_| |_|  \___|
        """

class WordleGame:
    def __init__(self, sheet):
        #sheet with 14885 5 letter words
        self.answers_sheet = sheet.worksheet('answer')
        #sheet with 2309 5 letter words
        self.words_sheet = sheet.worksheet('words')
        self.all_answers = self.answers_sheet.get_all_values()
        self.all_words = self.words_sheet.get_all_values()
        self.highscores_sheet = sheet.worksheet('highscores')
        self.highscores_data= self.highscores_sheet.get_all_values()
        self.player_name = None
        self.difficulty_choice = None
        

    def start_game(self):
        """
        Starts the game. Calls the get player name function then displays game page.
        """
        self.player_name = self.get_player_name()
        self.difficulty_choice = self.select_difficulty()
        
        print(f"Hello, {self.player_name}!")
        input("Press Enter to start the game")
        self.clear_terminal()
        print(title)
        

    def get_player_name(self):
        """
        Gets the player name and checks its length 
        """
        while True:
            name = input("Please enter your name: ")
            if len(name) > 2:
                return name.title()
            else:
                print("\rYour name must be at least 3 characters long. Please try again.", end="")
                
    def how_to_play(self):
        """
        Display how to play information
        """
        print(title)
        print("-" * 80)
        print("How to Play Wordle:")
        print("1. You will be asked to enter your name upon starting the game. Once your name is entered, the game will begin")
        print("2. You'll be asked to guess a 5-letter word. The game will provide feedback on your guess attempts.")
        print("3. The feedback consists of two elements: correct letters in the correct position and correct letters in the wrong position (*)")
        print("4. For example, if the secret word is 'APPLE' and you guess is 'ADOPT' the feedback might look like this:")
        print("   A _ _ P*_ as you can see the 'A' is in correct position with no marking and P is with an asterix idicating the letter is present in the word but in a different location")
        print("5. If you correctly guess the word within the specified number of attempts, you win the game!")
        print("6. You can choose to exit the game at any time")
        print("7. Have fun!")
        input("Press Enter to return to the main menu...")

    def select_difficulty(self):
        """
        Difficalty selector based on user input
        """
        print("Select difficulty:")
        print("e - Easy")
        print("n - Normal")
        print("h - Hard")
        while True:
            difficulty_choice = input("Enter choice (e/n/h): ").lower()
            if difficulty_choice in {"e", "n", "h"}:
                if difficulty_choice == "e":
                    print("You have selected easy difficulty. You will be given 10 attempts to guess the word.")
                    return "easy"
                elif difficulty_choice == "n":
                    print("You have selected normal difficulty. You will be given 6 attempts to guess the word.")
                    return "normal"
                elif difficulty_choice == "h":
                    print("You have selected hard difficulty. You will be given 4 attempts to guess the word.")
                    return "hard"
                break
            else:
                print("\rPlease enter a valid option (e, n, h).", end="")
                return self.select_difficulty()

    def get_num_guesses(self):
        if self.difficulty_choice == "easy":
            return 10
        elif self.difficulty_choice == "normal":
            return 6
        elif self.difficulty_choice == "hard":
            return 4
        
    def clear_terminal(self):
        """
        Clears terminal
        """
        # recovered from https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_highscores(self):#change this code
        """
        Show highscores data of the best 5 players
        The data is take from google sheets
        """
        print(title)
        print("-" * 80)
        print("Top 10 Highscores:")

        # Map difficulty levels to numerical values for sorting
        difficulty_mapping = {'easy': 1, 'normal': 2, 'hard': 3}
        # Skip the header row and convert numeric values for sorting
        highscores_data = [[row[0], row[1], int(row[2]), int(row[3])] for row in self.highscores_data[1:]]
        
        # Sorting function
        def sort_scores(score):
            name, difficulty, guesses, time = score
            return (guesses, difficulty_mapping[difficulty], time)
        
        # Sort the high_scores list
        sorted_highscores = sorted(highscores_data, key=sort_scores)
        
        top_10_highscores = sorted_highscores[:10]
        print(top_10_highscores)
        print("-" * 80)
        input("Press Enter to return to the main menu...")

    def add_highscore(self, player_name, difficulty, num_guesses, time_taken):
        """
        Add a new highscore to the highscores sheet.
        """
        new_highscore = [player_name, difficulty, num_guesses, time_taken]
        self.highscores_sheet.append_row(new_highscore)
        
def print_menu(firstload):
    """
    Function to display the main menu options and the ascii wordle title.
    Calls the corresponding functions for each option
    """
    if firstload:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title)
        print("-" * 80) 
        print("1. Start Game")
        print("2. Show High-Scores")
        print("3. How to play")
        print("-" * 80)
    
    menu_choice = input("Select an option : ").lower()
    return menu_choice


def main():
    """
    The main function to run the Wordle game.
    """
    #create an instance of the WordleGame class named game
    game = WordleGame(SHEET)
    #Set the flag of print_menu fuction to true for initally showing the whole menu
    firstload=True
    while True:
        # Display the menu and get the user's choice
        choice=print_menu(firstload)
        firstload= False # Set the flag to False after the first display
        if choice == "1":
            game.start_game()
            
        elif choice == "2":
            game.clear_terminal()
            game.show_highscores()
            firstload = True
            
        elif choice == "3":
            game.clear_terminal()
            game.how_to_play()
            firstload = True
            
        else:
            print("Invalid option. Please choose a valid option.")
            continue

if __name__ == "__main__":
    main()
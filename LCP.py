# Imports that are used in this script

import random, time
from datetime import datetime

# Declaration of basic variables that contains the help for LCP

LCPCurrentVersion = "Alpha v1.0.5"

LCPStartHelp = f'''Hello User! Welcome to the Lanzoor Command Panel (Version: {LCPCurrentVersion})! 
Type ?help to get help about the commands that you can use, or type ?exit to quit LCP.'''

LCPHelp = f'''Welcome to LCP command help! Here are the list of all commands that you can use.
?help: Open this help message.
?exit: Exit LCP.
?info: Open the information of LCP.
?updatelog: Open the update log.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?date: Get the current date based on your local timezone.
?time: Get the current time based on your local timezone.
?datetime: Get the current date and time based on your local timezone.'''

LCPInfo = f'''Welcome to LCP information page! Here are some informations about LCP.
Author: Lanzoor
Programming language: Python
Version (Current build): {LCPCurrentVersion}
First build: Alpha v1.0.0 in GMT+9 2024-04-06 3PM
Last updated: Now'''

LCPUpdateLog = f'''Welcome to the LCP update log page! Here are the log of updates that were
implemented in the LCP build.
Current version: {LCPCurrentVersion}
Alpha v1.0.0: The first build with basic commands like ?exit, ?help, and ?updatelog.
Alpha v1.0.1: The second build that added the ?rps command.
Alpha v1.0.2: Added the ?golt command.
Alpha v1.0.3: Added date and time commands.
Alpha v1.0.5: Reduced the rps function a bit, and 1.0.4 was just a simple bugfix'''

print(LCPStartHelp)

# Function declarations

def tryGoltInput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("You dumdum, that is not an integer!")
            
def golt():
    number = random.randint(0, 100)
    attempts = 0
    print(
        '''Let's play the \"Greater or lower than\" game!
        The rules are simple, I pick a random number between 1 and 100.
        If you make a guess, I'll tell you whenever your guess is greater than my guess, 
        or your guess is lower than my guess until you guess the value! Let's get started.''',
    )

    while True:
        inputValue = tryGoltInput("Enter your guess!\n>>> ")
        if inputValue > number:
            if inputValue <= 100:
                print(f"The number is lower than {inputValue}, try again!")
            attempts += 1
        elif inputValue < number:
            print(f"The number is greater than {inputValue}, try again!")
            attempts += 1
        elif inputValue == number:
            print(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game.")
        else:
            print("You dumdum, this number is out of the value!")
            attempts += 1
        break
    
def rps():
    UserChoice = input("Choose one! Rock, Paper, or Scissors!\n>>> ")
    CPUChoice = random.choice(["Rock", "Paper", "Scissors"])
    UserChoice = UserChoice.capitalize().replace(" ","")
    RpsChoice = ["Rock", "Paper", "Scissors"]
    
    while UserChoice not in RpsChoice:
        UserChoice = input("You dumdum, that is not a valid choice! Try again.\n>>> ")
    
    if CPUChoice == UserChoice:
        WinOrLose = "It's a draw!"
    else:
        WinningConditions = [
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock")
        ]

        if (UserChoice, CPUChoice) in WinningConditions:
            WinOrLose = "You won!"
        else:
            WinOrLose = "I won!"
    print(f"You picked {UserChoice}, I pick {CPUChoice}! {WinOrLose}")
        
def ordinal(n: int) -> str:
    return str(n) + ("th" if 11 <= (n % 100) <= 13 else (['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]))

# Command Inputs

while True:
    LCPInput = input(">>> ").replace(" ", "").lower()
    current_time = datetime.now()
    formatted_date = f"{current_time.strftime("%B")} {str(ordinal(int(current_time.strftime("%d"))))}{current_time.strftime(", %Y")}"
    formatted_time = current_time.strftime("%I:%M:%S %p")
    if LCPInput == "?exit":
        print("Exiting LCP...")
        time.sleep(0.5)
        print("You exitted the LCP!")
        break
    elif LCPInput == "?help":
        print(LCPHelp)
    elif LCPInput == "?info":
        print(LCPInfo)
    elif LCPInput == "?updatelog":
        print(LCPUpdateLog)
    elif LCPInput in ("?rps", "?rockpaperscissors"):
        rps()
    elif LCPInput in ("?golt", "?greaterorlowerthan"):
        golt()
    elif LCPInput == "?date":
        print(f"Your current date is {formatted_date}!")
    elif LCPInput == "?time":
        print(f"Your current time is {formatted_time}!")
    elif LCPInput == "?datetime":
        print(f"Your date and time is {formatted_time} {formatted_date}!")
    else:
        print(f"\"{LCPInput}\" is not a valid command, try something else!")
    # FIXME: Fix this fucking if-elif-else statement because it's hard to read
        
        
        
# NOTE: Some code of the program was reduced and improved by people in the Python Discord server

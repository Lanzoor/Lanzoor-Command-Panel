import random
from datetime import datetime

def tryIntInput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("You dumdum, that is not an integer!")
def golt(points: int):
    number = random.randint(0, 100)
    attempts = 0
    print(
        '''
Let's play the \"Greater or lower than\" game!
The rules are simple, I pick a random number between 1 and 100.
If you make a guess, I'll tell you whenever your guess is greater than my guess, 
or your guess is lower than my guess until you guess the value! Let's get started.
''',
    )

    while True:
        inputValue = tryIntInput("Enter your guess!\n  >>> ")
        if inputValue > number:
            if inputValue <= 100:
                print(f"The number is lower than {inputValue}, try again!")
            else:
                print("You dumdum, this number is out of the value!")
            attempts += 1
        elif inputValue < number:
            print(f"The number is greater than {inputValue}, try again!")
            attempts += 1
        elif inputValue == number:
            attempts += 1
            print(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game. You gained 5 points!")
            points += 5
            return points
            break
    
def rps(points: int):
    UserChoice = input("Choose one! Rock, Paper, or Scissors!\n  >>> ").capitalize().replace(" ","")
    CPUChoice = random.choice(["Rock", "Paper", "Scissors"])
    RpsChoice = ["Rock", "Paper", "Scissors"]
    while UserChoice not in RpsChoice:
        UserChoice = input("You dumdum, that is not a valid choice! Try again.\n  >>> ")
    if CPUChoice == UserChoice:
        WinOrLose = "It's a draw!"
        addingPoints = 2
    else:
        WinningConditions = [
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock")
        ]
        if (UserChoice, CPUChoice) in WinningConditions:
            WinOrLose = "You won!"
            addingPoints = 3
        else:
            WinOrLose = "I won!"
            addingPoints = 1
    points += addingPoints
    print(f"You picked {UserChoice}, I pick {CPUChoice}! {WinOrLose} You gained {addingPoints} points in this game.")
    return points

def ordinal(n: int) -> str:
    if 11 <= n % 100 <= 13: return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def isLeapYear(year: int = int(datetime.now().strftime("%Y"))) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

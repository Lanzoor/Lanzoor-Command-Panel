import random, sys
from datetime import datetime
from time import sleep

def tryIntInput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            printAnimation("You dumdum, that is not an integer!")
def golt(points: int):
    number = random.randint(0, 100)
    attempts = 0
    printAnimation(
        '''
Let's play the \"Greater or lower than\" game!
The rules are simple, I pick a random number between 1 and 100.
If you make a guess, I'll tell you whenever your guess is greater than my guess, 
or your guess is lower than my guess until you guess the value! Let's get started.
''',
    )

    while True:
        inputValue = tryIntInput("Enter your guess!\n  >>> ")
        attempts += 1
        
        if not (1 <= number <= 100):
            printAnimation("You dumdum, that value is out of the range! Try a value that is in the range 1 ~ 100.")
        elif inputValue > number and not (inputValue > 100):
            printAnimation(f"The number is lower than {inputValue}, try again!")
        elif inputValue < number and not (inputValue < 1):
            printAnimation(f"The number is greater than {inputValue}, try again!")
        elif inputValue == number:
            printAnimation(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game. You gained 5 points!")
            points += 5
            return points
    
def rps(points: int):
    UserChoice = input("Choose one! Rock, Paper, or Scissors!\n  >>> ").capitalize().replace(" ","")
    RpsChoice = ["Rock", "Paper", "Scissors"]
    CPUChoice = random.choice(RpsChoice)
    
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
    printAnimation(f"You picked {UserChoice}, I pick {CPUChoice}! {WinOrLose} You gained {addingPoints} points in this game.")
    return points

def ordinal(n: int) -> str:
    if 11 <= n % 100 <= 13: return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def isLeapYear(year: int = int(datetime.now().strftime("%Y"))) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def printAnimation(message: str, delay: float | int = 0.001) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()

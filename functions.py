import random, sys
from datetime import datetime
from time import sleep

def tryIntInput(prompt: str) -> int:
    while True:
        try:
            return int(inputAnimation(prompt))
        except:
            printAnimation("You dumdum, that is not an integer!")
def golt(points: int, multi: int):
    number = random.randint(1, 100)
    attempts = 0
    printAnimation(
        '''
Let's play the \"Greater or lower than\" game!
The rules are simple, I pick a random number between 1 and 100.
If you make a guess, I'll tell you whenever your guess is greater than my guess, 
or your guess is lower than my guess until you guess the value! Also type exit to just... exit the game.
''',
    )

    while True:
        inputValue = inputAnimation("Enter your guess!\n  >>> ")
        if inputValue == "exit": 
            return points
        try: 
            inputValue = int(inputValue)
        except:
            printAnimation("You dumdum, that is not an integer!")
            continue
        attempts += 1
        
        if not (1 <= number <= 100):
            printAnimation("You dumdum, that value is out of the range! Try a value that is in the range 1 ~ 100.")
        elif inputValue > number and not (inputValue > 100):
            printAnimation(f"The number is lower than {inputValue}, try again!")
        elif inputValue < number and not (inputValue < 1):
            printAnimation(f"The number is greater than {inputValue}, try again!")
        elif inputValue == number:
            printAnimation(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game. You gained {7 * multi} points!")
            points += 7 * multi
            return points
    
def rps(points: int, multi: int):
    UserChoice = inputAnimation("Choose one! Rock, Paper, or Scissors!\n  >>> ").capitalize().replace(" ","")
    RpsChoice = ["Rock", "Paper", "Scissors"]
    CPUChoice = random.choice(RpsChoice)
    
    while UserChoice not in RpsChoice:
        UserChoice = inputAnimation("You dumdum, that is not a valid choice! Try again.\n  >>> ").capitalize().replace(" ","")
    
    if CPUChoice == UserChoice:
        WinOrLose = "It's a draw!"
        addingPoints = 2 * multi
    else:
        WinningConditions = [
            ("Rock", "Scissors"),
            ("Scissors", "Paper"),
            ("Paper", "Rock"),
        ]
        if (UserChoice, CPUChoice) in WinningConditions:
            WinOrLose = "You won!"
            addingPoints = 3 * multi
        else:
            WinOrLose = "I won!"
            addingPoints = 1 * multi
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
    
def inputAnimation(message: str, delay: float | int = 0.001) -> str:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    return input("")

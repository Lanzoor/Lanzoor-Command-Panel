import random

def tryIntInput(prompt: str) -> int:
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
        inputValue = tryIntInput("Enter your guess!\n>>> ")
        if inputValue > number:
            if inputValue <= 100:
                print(f"The number is lower than {inputValue}, try again!")
            attempts += 1
        elif inputValue < number:
            print(f"The number is greater than {inputValue}, try again!")
            attempts += 1
        elif inputValue == number:
            print(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game.")
            break
        else:
            print("You dumdum, this number is out of the value!")
            attempts += 1
    
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

    print(f"You picked {UserChoice}, I pick {CPUChoice}! {WinOrLose}")
        
def ordinal(n: int) -> str:
    return str(n) + ("th" if 11 <= (n % 100) <= 13 else (['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]))

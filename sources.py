import random, sys
from datetime import datetime
from time import sleep

def try_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input_with_animation(prompt))
        except:
            print_with_animation("You dumdum, that is not an integer!")
def golt(points: int, multi: int, mulmul: int):
    number = random.randint(1, 100)
    attempts = 0
    print_with_animation(
        '''
Let's play the \"Greater or lower than\" game!
Type 'help' to know how to play!
''')

    while True:
        user_guess = input_with_animation("Enter your guess!\n  >>> ")
        if user_guess == "exit": 
            return points
        elif user_guess == "help":
            print('''
The rules are simple, I pick a random number between 1 and 100.
If you make a guess, I'll tell you whenever your guess is greater than my guess, 
or your guess is lower than my guess until you guess the value!
''')
            continue
        try: 
            user_guess = int(user_guess)
        except:
            print_with_animation("You dumdum, that is not an integer!")
            continue
        attempts += 1
        
        if not (1 <= number <= 100):
            print_with_animation("You dumdum, that value is out of the range! Try a value that is in the range 1 ~ 100.")
        elif user_guess > number and not (user_guess > 100):
            print_with_animation(f"The number is lower than {user_guess}, try again!")
        elif user_guess < number and not (user_guess < 1):
            print_with_animation(f"The number is greater than {user_guess}, try again!")
        elif user_guess == number:
            print_with_animation(f"You've guessed it right! The answer was {number}, and you used {attempts} attempts in this game. You gained {30 * multi * mulmul} points!")
            points += 45 * multi * mulmul
            return points
    
def rps(points: int, multi: int, mulmul: int):
    user_choice = input_with_animation("Choose one! Rock, Paper, or Scissors!\n  >>> ").capitalize().replace(" ","")
    valid_rps_choice = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(valid_rps_choice)
    
    while user_choice not in valid_rps_choice:
        user_choice = input_with_animation("You dumdum, that is not a valid choice! Try again.\n  >>> ").capitalize().replace(" ","")
    
    if computer_choice == user_choice:
        did_i_win_or_lose = "It's a draw!"
        adding_points = 6 * multi * mulmul
    else:
        conditions_of_winning = [
            ("Rock", "Scissors"),
            ("Scissors", "Paper"),
            ("Paper", "Rock"),
        ]
        if (user_choice, computer_choice) in conditions_of_winning:
            did_i_win_or_lose = "You won!"
            adding_points = 12 * multi * mulmul
        else:
            did_i_win_or_lose = "I won!"
            adding_points = 4 * multi * mulmul
    points += adding_points
    print_with_animation(f"You picked {user_choice}, I pick {computer_choice}! {did_i_win_or_lose} You gained {adding_points} points in this game.")
    return points

def ordinal(n: int) -> str:
    if 11 <= n % 100 <= 13: 
        return str(n) + "th"
    return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def is_leap_year(year: int = int(datetime.now().strftime("%Y"))) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def print_with_animation(message: str, delay: float | int = 0.001, end_with_newline = True) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    if end_with_newline:
        print()
    
def input_with_animation(message: str, delay: float | int = 0.001) -> str:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    return input("")

currentver = "1.1.6"

welcome = f'''
Hello User! Welcome to the Lanzoor Command Panel (Version: {currentver})! 
Type ?help to get help about the commands that you can use, or type ?exit to exit LCP.'''

help = f'''
Welcome to LCP help!
LCP is a point-based game where you gain points by playing games.
Here is the information about LCP.
Author: Lanzoor
Programming language: Python (3.12~)
Version (Current version): {currentver}
First version: Alpha v1.0 in GMT+9 2024-04-06 3PM 
You can exit the importing process, shop, and the greater or lower than (golt) by typing exit.

You can also use these commands:
?help: Open this help message.
?exit: Exit LCP.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?datetime: Get the current date and time based on your local timezone.
?ping: Check the print latency...for some reason because Lanzoor thought that this was a funny idea-
?randint: Pick a random value between the maximum and minimum value that you input.
?randkey: Generate a random key based on the length.
?stats or ?stat: Show the user stats.
?flipacoin: Flip a coin.
?shop: Open the shop.
?import: Import a save file.
?export: Export a save file.'''

valid_commands = [
    "help",
    "exit",
    "rps",
    "rockpaperscissors",
    "golt",
    "greaterorlessthan",
    "datetime",
    "ping",
    "randint",
    "randkey",
    "stats",
    "stat",
    "flipacoin",
    "shop",
    "import",
    "export"
]

welcome_to_the_shop = '''
Hello there! Welcome to the shop. In here you can spend points to get upgrades.
Type exit to exit the shop. Here is the list of items that you can buy. 
Type the corresponding number to buy the item!'''

exit_confirmation = '''
Are you sure you want to leave LCP? All of your data will be lost. 
However, your save data can be imported and exported using the import and the export 
commands. You can simply enter Y to leave if you belive that your current
save data is stored somewhere secure, and just enter nothing else than Y
to cancel the exitting process.
>>> '''

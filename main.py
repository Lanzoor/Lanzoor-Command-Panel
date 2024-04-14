# Imports that are used in this script

import random, time, timeit
from datetime import datetime
from functions import *

# Declaration of basic variables that contains the help for LCP

CurrentVersion = "Beta 1.2"

StartHelp = f'''
Hello User! Welcome to the Lanzoor Command Panel (Version: {CurrentVersion})! 
Type ?help to get help about the commands that you can use, or type ?exit to quit LCP.
'''

Help = '''
Welcome to LCP command help! Here are the list of all commands that you can use.
?help: Open this help message.
?starthelp: Open the start help message again.
?exit: Exit LCP.
?info: Open the information of LCP.
?updatelog: Open the update log.
?rps or ?rockpaperscissors: Play the Rock Paper Scissors game.
?golt or ?greaterorlowerthan: Play the "Greater or Lower than" game.
?date: Get the current date based on your local timezone.
?time: Get the current time based on your local timezone.
?datetime: Get the current date and time based on your local timezone.
?ping: Pong!
?randint: Pick a random value between the maximum and minimum value that you input.
?randkey: Generate a random key based on the length.
?flipacoin: Flip a coin.
'''

Info = f'''
Welcome to LCP information page! Here are some informations about LCP.
Author: Lanzoor
Programming language: Python
Version (Current build): {CurrentVersion}
First build: Alpha v1.0 in GMT+9 2024-04-06 3PM
'''

UpdateLog = f'''
Welcome to the LCP update log page! Here are the log of updates that were
implemented in the LCP build. Also minor updates are not included here, because it was really, really small.
Current version: {CurrentVersion}
Alpha v1.0: The first build with basic commands like ?exit, ?help, and ?updatelog.
Alpha v1.1: The second build that added the ?rps command.
Alpha v1.2: Added the ?golt command.
Alpha v1.3: Added date and time commands.
Alpha v1.4: Added the ?randint command.
Beta v1.0: The first beta build with a more detailed executing indicator,
?ping function, and handmade ordinal function.
Beta v1.1: The second beta build that fixed the code mayhem.
Beta v1.2: A major update that adjusted a lot about the code, and added more commands.
Beta v1.3: Added the ?starthelp command and adjusted the code a bit.
'''

print("Initializing Program...\n")
time.sleep(0.25)
print("Executing LCP...")
time.sleep(0.25)
print(StartHelp)

# Command Inputs

while True:
    UserInput = str(input(">>> "))
    FormattedUserInput = UserInput.replace(" ", "").lower()
    current_time = datetime.now()
    formatted_date = f"{current_time.strftime("%B")} {str(ordinal(int(current_time.strftime("%d"))))}{current_time.strftime(", %Y")}"
    formatted_time = current_time.strftime("%I:%M:%S %p")
    match FormattedUserInput:
        case "?exit":
            print("Exiting LCP...")
            time.sleep(0.25)
            print("You exitted the LCP!")
            break
        case "?help":
            print(Help)
        case "?starthelp":
            print(StartHelp)
        case "?info":
            print(Info)
        case "?updatelog":
            print(UpdateLog)
        case ("?rps" | "?rockpaperscissors"):
            rps()
        case ("?golt" | "?greaterorlowerthan"):
            golt()
        case "?date":
            print(f"Your current date is {formatted_date}!\nIsLeapYear: {isLeapYear()}\nYour local timezone: {datetime.now().astimezone().strftime("%Z")}")
        case "?time":
            print(f"Your current time is {formatted_time}!")
        case "?datetime":
            print(f"Your date and time are {formatted_time} {formatted_date}!\nIsLeapYear: {isLeapYear()}\nYour local timezone: {datetime.now().astimezone().strftime("%Z")}")
        case "?ping":
            latency = timeit.timeit("print('Pong!')", number = 1)
            print(f"Latency of the command input was {latency * 1000}ms!")
        case "?randint":
            x = tryIntInput("Choose your minimum number!\n  >>> ")
            y = tryIntInput("Choose your maximum number!\n  >>> ")
            print(f"My random choice between {x} and {y} is {random.randint(x, y)}!")
        case "?randkey":
            length = tryIntInput("Enter the length of a key generation!\n  >>> ")
            result = ""
            char = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            for _ in range(0, length):
                if _ % 4 == 0 and _ != 0:
                    result += "-"
                result += random.choice(char)
            print(f"Your random key that has {length} letters is {result}!")
        case "?flipacoin":
            print(f"I flipped a coin... it landed on {random.choice(["Heads", "Tails"])}!")
        case "":
            print("Uhm, try typing something?")
        case _:
            print(f"\"{UserInput}\" is not a valid command, try again!")
